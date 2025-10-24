#!/usr/bin/env python3
"""
Ultra-Simple Crochet Image Manager
Just tell me what image to change, I handle everything else automatically.
"""

import os
import json
import requests
from pathlib import Path
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image

class CrochetImageManager:
    """Dead simple - you say change image, I do everything"""
    
    def __init__(self):
        load_dotenv()
        
        self.root = Path(__file__).parent
        self.assets_dir = self.root / "assets"
        self.db_file = self.root / "crochet-images.json"
        
        # Initialize OpenAI with gpt-image-1
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("Need OPENAI_API_KEY in .env file")
        
        self.client = OpenAI(api_key=api_key)
        self.db = self.load_db()
        
        # Pre-defined crochet prompts - no thinking required
        self.prompts = {
            'hero-main': "Cozy artisan crafting flatlay with premium crochet supplies on creamy linen fabric, warm terracotta accents (#D28F75), soft blush and sage green yarns, handcrafted wooden crochet hooks, delicate finished projects, dried flowers, warm natural lighting, cozy handmade aesthetic, artisan lifestyle photography",
            
            'hero-alt': "Gentle hands working on beautiful crochet project with soft blush-colored yarn, detailed stitchwork visible, cozy artisan home setting with warm natural lighting, ceramic mug nearby, peaceful crafting moment, warm lifestyle photography",
            
            'value-yarn': "Extreme close-up of luxury yarn fibers showing incredible texture, mix of alpaca and merino wool in soft blush, sage green, and cream colors, individual fibers visible, warm natural lighting, artistic macro photography",
            
            'value-patterns': "Clean flat lay of detailed crochet pattern pages with clear diagrams, professional layout, surrounded by matching teal yarn and silver hooks, educational aesthetic, bright clean lighting",
            
            'value-complete': "Perfect flat lay of complete crochet kit contents: premium yarns, hooks, pattern book, stitch markers, measuring tape, project bag, arranged in organized grid on white background, professional product photography",
            
            'product-beginner': "Beginner crochet kit with soft pastel yarns, basic hooks, simple pattern booklet, everything in premium gift box with teal ribbon, clean product photography on white background",
            
            'product-intermediate': "Intermediate crochet kit with jewel-tone yarns including teal, multiple hook sizes, detailed pattern book, cable needles, elegant flat lay composition",
            
            'product-advanced': "Luxury advanced crochet kit with premium alpaca yarns, professional interchangeable hooks, complex lace pattern, blocking mats, sophisticated presentation",
            
            'lifestyle-home': "Beautiful cozy living room with handmade crochet throw blanket in soft terracotta and cream tones on linen sofa, dried flowers, natural textures, warm natural lighting, artisan home decor aesthetic",
            
            'lifestyle-crafting': "Person enjoying crochet in comfortable armchair by window, natural lighting, cozy atmosphere, teal yarn project in progress, peaceful crafting moment",
            
            'testimonial-1': "Happy woman in her 40s holding beautiful finished crochet blanket, genuine smile, cozy home background, natural lighting, authentic moment of pride and accomplishment",
            
            'testimonial-2': "Diverse woman in her 30s working on crochet project, focused and content expression, modern home setting, soft lighting, authentic crafting scene",
            
            'testimonial-3': "Senior woman with finished crochet scarf, warm smile, comfortable home environment, showing craftsmanship and satisfaction, natural portrait lighting",
            
            'process-quality': "Hands carefully inspecting premium yarn quality, checking softness and consistency, professional clean environment, attention to detail and craftsmanship",
            
            'process-packing': "Crochet kits being carefully packed in branded boxes with tissue paper, attention to premium unboxing experience, clean organized workspace",
            
            'social-og': "Social media banner with cozy crochet scene background, teal branding colors, professional layout for Facebook/Instagram sharing, 1200x630 dimensions",
            
            'social-square': "Instagram-ready square image of beautiful crochet project in progress, teal yarns, aesthetic flat lay, perfect for social media, 1080x1080"
        }
        
        print("🧶 Crochet Image Manager Ready - Just tell me what to change!")
    
    def load_db(self):
        """Load image database"""
        if self.db_file.exists():
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {"images": {}, "last_updated": None}
    
    def save_db(self):
        """Save image database"""
        self.db["last_updated"] = datetime.now().isoformat()
        with open(self.db_file, 'w') as f:
            json.dump(self.db, f, indent=2)
    
    def generate_alt_text(self, image_name, prompt):
        """Generate perfect alt text automatically"""
        
        alt_texts = {
            'hero-main': "Cozy modern crafting room with premium crochet supplies and teal accents",
            'hero-alt': "Hands crocheting with premium teal yarn in peaceful home setting",
            'value-yarn': "Close-up of luxury alpaca and merino wool yarn fibers in teal tones",
            'value-patterns': "Professional crochet pattern diagrams with matching yarn and tools",
            'value-complete': "Complete crochet kit contents organized on white background",
            'product-beginner': "Beginner crochet kit with pastel yarns in premium gift box",
            'product-intermediate': "Intermediate crochet kit with jewel-tone yarns and multiple tools",
            'product-advanced': "Luxury advanced crochet kit with premium alpaca yarns",
            'lifestyle-home': "Modern living room with handmade teal crochet throw blanket",
            'lifestyle-crafting': "Person enjoying peaceful crochet time by sunny window",
            'testimonial-1': "Happy customer holding beautiful finished crochet blanket",
            'testimonial-2': "Satisfied crocheter working on project in modern home",
            'testimonial-3': "Senior woman proudly displaying handmade crochet scarf",
            'process-quality': "Hands inspecting premium yarn quality for consistency",
            'process-packing': "Crochet kits being carefully packed with premium presentation",
            'social-og': "Crochet kit brand image for social media sharing",
            'social-square': "Beautiful crochet work in progress for Instagram"
        }
        
        return alt_texts.get(image_name, f"Professional crochet image for {image_name.replace('-', ' ')}")
    
    def generate_image(self, image_name):
        """Generate image - completely automatic"""
        
        prompt = self.prompts.get(image_name, "Professional crochet crafting scene with teal accents")
        
        print(f"🎨 Generating: {image_name}")
        print(f"📝 Using: {prompt[:100]}...")
        
        try:
            response = self.client.images.generate(
                model="dall-e-3",  # Using DALL-E 3 (gpt-image-1 requires org verification)
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )
            
            image_url = response.data[0].url
            img_response = requests.get(image_url)
            img_response.raise_for_status()
            
            return img_response.content
            
        except Exception as e:
            print(f"❌ Generation failed: {e}")
            raise
    
    def save_image(self, image_name, image_data):
        """Save image in multiple sizes for Shopify"""
        
        # Ensure assets directory exists
        self.assets_dir.mkdir(exist_ok=True)
        
        # Save original first
        temp_path = self.assets_dir / f"{image_name}_temp.jpg"
        
        with open(temp_path, 'wb') as f:
            f.write(image_data)
        
        try:
            with Image.open(temp_path) as img:
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Generate sizes Shopify needs
                sizes = [
                    (1920, f"{image_name}_hero.jpg"),     # Hero images
                    (800, f"{image_name}.jpg"),           # Main image
                    (600, f"{image_name}_600w.jpg"),      # Medium
                    (400, f"{image_name}_400w.jpg")       # Small/mobile
                ]
                
                saved_files = []
                
                for width, filename in sizes:
                    aspect_ratio = img.height / img.width
                    height = int(width * aspect_ratio)
                    
                    resized = img.resize((width, height), Image.Resampling.LANCZOS)
                    save_path = self.assets_dir / filename
                    
                    resized.save(save_path, 'JPEG', quality=85, optimize=True)
                    saved_files.append(str(save_path))
                    print(f"✅ Saved: {filename}")
                
                # Clean up temp
                temp_path.unlink()
                
                # Return main path
                return str(self.assets_dir / f"{image_name}.jpg")
                
        except Exception as e:
            print(f"❌ Processing failed: {e}")
            # Fallback
            main_path = self.assets_dir / f"{image_name}.jpg"
            temp_path.rename(main_path)
            return str(main_path)
    
    def update_image(self, image_name):
        """Complete workflow - you just say the name, I do everything"""
        
        print(f"\n🧶 Updating {image_name}...")
        
        # Generate image
        image_data = self.generate_image(image_name)
        
        # Save in multiple sizes
        image_path = self.save_image(image_name, image_data)
        
        # Generate alt text
        alt_text = self.generate_alt_text(image_name, self.prompts.get(image_name, ""))
        
        # Update database
        self.db["images"][image_name] = {
            "filename": f"{image_name}.jpg",
            "path": image_path,
            "alt_text": alt_text,
            "generated": datetime.now().isoformat(),
            "shopify_ready": True
        }
        
        self.save_db()
        
        print(f"✅ {image_name} ready!")
        print(f"📁 Saved to: assets/{image_name}.jpg")
        print(f"🏷️  Alt text: {alt_text}")
        print(f"📋 Next: Upload assets/{image_name}.jpg to Shopify admin → Settings → Files")
        print(f"🔗 Then use: shopify://shop_images/{image_name}.jpg in templates")
        
        return True
    
    def list_images(self):
        """Show all available images"""
        
        print("\n🧶 Available Crochet Images:")
        print("=" * 50)
        
        categories = {
            'Hero Images': ['hero-main', 'hero-alt'],
            'Value Props': ['value-yarn', 'value-patterns', 'value-complete'],
            'Products': ['product-beginner', 'product-intermediate', 'product-advanced'],
            'Lifestyle': ['lifestyle-home', 'lifestyle-crafting'],
            'Testimonials': ['testimonial-1', 'testimonial-2', 'testimonial-3'],
            'Process': ['process-quality', 'process-packing'],
            'Social Media': ['social-og', 'social-square']
        }
        
        for category, images in categories.items():
            print(f"\n📂 {category}:")
            for img in images:
                status = "✅ Generated" if img in self.db["images"] else "⏳ Available"
                print(f"   {img} - {status}")
                if img in self.db["images"]:
                    print(f"      Alt: {self.db['images'][img]['alt_text']}")

def main():
    """Ultra simple CLI - just the essentials"""
    
    import sys
    
    try:
        manager = CrochetImageManager()
        
        if len(sys.argv) < 2:
            print("\n🧶 Crochet Image Manager")
            print("Usage:")
            print("  python crochet_images.py <image-name>    # Generate/update image")
            print("  python crochet_images.py list            # Show all available images")
            print("\nExamples:")
            print("  python crochet_images.py hero-main")
            print("  python crochet_images.py product-beginner")
            manager.list_images()
            return
        
        command = sys.argv[1]
        
        if command == 'list':
            manager.list_images()
        elif command in manager.prompts:
            manager.update_image(command)
        else:
            print(f"❌ Unknown image: {command}")
            print("Run 'python crochet_images.py list' to see available images")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
