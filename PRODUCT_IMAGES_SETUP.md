# Setting Up Product Images for Testimonials

## Generated Images
The following finished crochet product images have been generated and are ready to use:

1. **finished-blanket.jpg** - Beautiful finished crochet blanket in soft blush and cream colors
2. **finished-scarf.jpg** - Elegant finished crochet scarf in sage green with lace pattern  
3. **finished-bag.jpg** - Handmade crochet tote bag in teal with geometric pattern

## Upload Instructions

### Step 1: Upload Images to Shopify
1. Go to your Shopify admin panel
2. Navigate to **Settings** → **Files**
3. Click **Upload files**
4. Upload these files from the `assets/` folder:
   - `finished-blanket.jpg`
   - `finished-scarf.jpg` 
   - `finished-bag.jpg`

### Step 2: Configure Testimonials Section
1. In your Shopify admin, go to **Online Store** → **Themes**
2. Click **Customize** on your active theme
3. Navigate to the page with the **Crochet Testimonials** section
4. For each testimonial block:
   - Click on the testimonial to edit
   - Scroll down to **Finished Product Image**
   - Select the appropriate uploaded image
   - Update the **Product Name** and **Product Image Alt Text** as needed

### Recommended Image Assignments
- **Sarah M.** testimonial → `finished-blanket.jpg` (Cozy Blanket)
- **Jessica L.** testimonial → `finished-scarf.jpg` (Elegant Scarf)
- **Maria R.** testimonial → `finished-bag.jpg` (Stylish Tote Bag)

## Layout Features
- Product images appear on the right side of each testimonial
- Images are automatically sized and responsive
- On mobile, images stack below the testimonial text
- Clean, professional presentation that showcases finished products

## Additional Images Available
If you need more product images, you can generate them using:
```bash
python crochet_images.py finished-hat
python crochet_images.py finished-cardigan
```

The testimonials section now beautifully showcases both customer reviews and the finished products they created!
