# Shopify Theme Development Guide

## Prerequisites ✅
- Shopify Partner account (registered)
- Shopify CLI installed
- Code editor (VS Code recommended)
- Basic knowledge of HTML, CSS, JavaScript, and Liquid

## Overview
As a Shopify Partner, you can create custom themes for merchants or for the Theme Store. This guide covers the complete development workflow.

## Quick Start for Students 🚀

**Already have a development store? Jump straight to development:**

```bash
# 1. Create project directory
mkdir my-shopify-theme
cd my-shopify-theme

# 2. Authenticate (if not done already)
shopify auth login

# 3. List themes on your store
shopify theme list --store your-store.myshopify.com

# 4. Pull existing theme (use ID from step 3, without #)
shopify theme pull --store your-store.myshopify.com --theme THEME_ID

# 5. Start development server
shopify theme dev --store your-store.myshopify.com
```

**Need a development store first?** Continue reading from Step 1.

## Step 1: Set Up Development Store

### Create a Development Store
1. Log into your [Shopify Partner Dashboard](https://partners.shopify.com/)
2. Navigate to **Stores** → **Add store**
3. Select **Development store**
4. Fill in store details:
   - Store name
   - Store URL
   - Purpose (Theme development)
5. Click **Save**

### Access Your Development Store
- Once created, you'll get admin access to test your theme
- Use this store for all theme development and testing

## Step 2: Initialize Your Theme Project

### Option A: Start from Scratch
```bash
# Navigate to your project directory
cd /path/to/your/project

# Initialize a new theme
shopify theme init

# Follow the prompts to name your theme
```

### Option B: Start with Dawn (Recommended)
```bash
# Clone Shopify's reference theme
shopify theme init --clone-url https://github.com/Shopify/dawn.git

# Or use the shorthand
shopify theme init dawn
```

### Option C: Pull Existing Theme
```bash
# List available themes from your store
shopify theme list --store your-store.myshopify.com

# Pull a specific theme (use the ID from the list command)
shopify theme pull --store your-store.myshopify.com --theme THEME_ID
```

## Step 3: Understanding Theme Structure

After pulling a theme, you'll see this structure:
```
theme/
├── assets/           # CSS, JS, images, fonts
├── blocks/           # Theme blocks (Shopify 2.0)
├── config/           # Theme settings and data
├── layout/           # Base templates (theme.liquid)
├── locales/          # Translation files
├── sections/         # Reusable content blocks
├── snippets/         # Reusable code fragments
├── templates/        # Page templates
└── templates/customers/  # Customer account templates
```

### Key Files to Know:
- `layout/theme.liquid` - Main HTML structure (the wrapper for all pages)
- `templates/index.liquid` - Homepage template
- `templates/product.liquid` - Product page template
- `templates/collection.liquid` - Collection/category page template
- `config/settings_schema.json` - Theme customization options
- `assets/application.css.liquid` - Main CSS file
- `assets/application.js` - Main JavaScript file

### Modern Theme Features (Shopify 2.0):
- **`blocks/`** - Individual content blocks that can be added to sections
- **`sections/`** - Page sections that can contain multiple blocks
- **Dynamic sections** - Sections can be added/removed via the theme editor
- **JSON templates** - Some templates may be `.json` files instead of `.liquid`

### What Each Directory Contains:
- **Assets**: All static files (images, CSS, JS, fonts)
- **Blocks**: Reusable content blocks for sections
- **Config**: Theme settings, color schemes, and data files
- **Layout**: The base HTML structure that wraps all pages
- **Locales**: Translation files for multi-language stores
- **Sections**: Large content areas (header, footer, product sections)
- **Snippets**: Small reusable pieces of code
- **Templates**: Full page layouts for different page types

## Step 4: Connect to Your Development Store & Pull Existing Theme

### Authenticate with Shopify
```bash
# Login to your partner account (if not already logged in)
shopify auth login
```

### Pull an Existing Theme (Complete Example)
If you want to work on an existing theme from your store:

```bash
# 1. Navigate to your project directory
cd /path/to/your/project

# 2. List all themes on your store to find the one you want
shopify theme list --store your-store.myshopify.com

# Example output:
# ╭─ info ──────────────────────────────────────────────╮
# │  name                             role       id     │
# │  ───────────────────────────────  ────────   ─────  │
# │  Horizon                          [live]     #1364  │
# │                                              56470  │
# │                                              615    │
# ╰─────────────────────────────────────────────────────╯

# 3. Pull the theme using the ID (without the # symbol)
shopify theme pull --store your-store.myshopify.com --theme 136456470615

# 4. The CLI will ask if you want to proceed if not in a theme directory
# Answer: Yes, confirm
```

### Development Server
After pulling your theme, start the development server:
```bash
# Connect your theme to a specific store for development
shopify theme dev --store your-store.myshopify.com
```

The `shopify theme dev` command:
- Starts a local development server
- Syncs changes in real-time
- Provides hot reloading
- Shows detailed error messages
- Creates a development copy (won't affect your live theme)

## Step 5: Theme Development Workflow

### 1. Local Development
```bash
# Start development server
shopify theme dev --store your-store.myshopify.com

# This will:
# - Upload your theme as a development theme
# - Start watching for file changes
# - Provide a preview URL
```

### 2. File Structure Best Practices

#### CSS Organization
```scss
// assets/application.css.liquid
/* Base styles */
@import 'base/variables';
@import 'base/typography';

/* Components */
@import 'components/buttons';
@import 'components/forms';

/* Templates */
@import 'templates/product';
@import 'templates/collection';
```

#### JavaScript Organization
```javascript
// assets/application.js
// Main theme functionality
document.addEventListener('DOMContentLoaded', function() {
  // Initialize theme features
});
```

### 3. Liquid Template Development

#### Basic Liquid Syntax
```liquid
<!-- Variables -->
{{ product.title }}
{{ product.price | money }}

<!-- Loops -->
{% for product in collection.products %}
  <h3>{{ product.title }}</h3>
{% endfor %}

<!-- Conditionals -->
{% if product.available %}
  <button>Add to Cart</button>
{% else %}
  <span>Sold Out</span>
{% endif %}

<!-- Include snippets -->
{% render 'product-card', product: product %}
```

## Step 6: Theme Testing

### Local Testing Checklist
- [ ] Test on mobile and desktop
- [ ] Check all page templates
- [ ] Verify cart functionality
- [ ] Test checkout process
- [ ] Validate theme settings
- [ ] Check performance scores

### Performance Testing
```bash
# Use Shopify's theme inspector
shopify theme check

# Check for accessibility and performance issues
```

## Step 7: Deployment Options

### Push to Live Theme
```bash
# Push to main theme (be careful!)
shopify theme push --store your-store.myshopify.com

# Push to a new unpublished theme
shopify theme push --store your-store.myshopify.com --unpublished
```

### Share Development Theme
```bash
# Share preview link with clients
shopify theme share --store your-store.myshopify.com
```

## Step 8: Theme Store Submission (Optional)

### Preparing for Theme Store
1. **Code Quality**
   - Follow Shopify's theme requirements
   - Use semantic HTML
   - Ensure accessibility compliance
   - Optimize performance

2. **Documentation**
   - Create setup instructions
   - Document customization options
   - Provide support documentation

3. **Testing**
   - Test across multiple browsers
   - Verify mobile responsiveness
   - Check with various content types

### Submission Process
1. Navigate to Partner Dashboard
2. Go to **Themes** → **Submit theme**
3. Upload theme ZIP file
4. Fill in theme details and pricing
5. Submit for review

## Essential Commands Reference

```bash
# Authentication
shopify auth login

# Theme initialization
shopify theme init [theme-name]
shopify theme init --clone-url [git-url]

# Development
shopify theme dev --store [store-url]
shopify theme check
shopify theme console

# Theme management
shopify theme list --store [store-url]
shopify theme pull --store [store-url] --theme [theme-id]
shopify theme push --store [store-url]
shopify theme push --store [store-url] --unpublished

# Sharing
shopify theme share --store [store-url]
```

## Best Practices

### 1. Code Organization
- Use consistent naming conventions
- Modularize CSS and JavaScript
- Comment your code thoroughly
- Use version control (Git)

### 2. Performance
- Optimize images and assets
- Minimize HTTP requests
- Use lazy loading for images
- Implement critical CSS

### 3. Accessibility
- Use semantic HTML elements
- Provide alt text for images
- Ensure keyboard navigation
- Test with screen readers

### 4. Mobile-First Design
- Start with mobile layouts
- Use responsive design principles
- Test on real devices
- Consider touch interactions

## Troubleshooting

### Common CLI Issues

#### 1. "Nonexistent flag: --theme-id"
**Problem**: Using incorrect flag for theme ID
**Solution**: Use `--theme` instead of `--theme-id`
```bash
# ❌ Wrong
shopify theme pull --store your-store.myshopify.com --theme-id 123456

# ✅ Correct  
shopify theme pull --store your-store.myshopify.com --theme 123456
```

#### 2. "It doesn't seem like you're running this command in a theme directory"
**Problem**: CLI warning when pulling theme to empty directory
**Solution**: This is normal - just confirm "Yes" to proceed

#### 3. Authentication Issues
**Problem**: CLI not authenticated or wrong account
**Solutions**:
```bash
# Check current authentication
shopify whoami

# Re-authenticate if needed
shopify auth logout
shopify auth login
```

#### 4. Store Access Issues
**Problem**: Can't access development store
**Solutions**:
- Ensure you're using the correct store URL format: `store-name.myshopify.com`
- Verify you have access to the store in your Partner Dashboard
- Check if the store is paused or has restrictions

### Common Development Issues
1. **Theme not syncing**: Check internet connection and store permissions
2. **Liquid errors**: Use `shopify theme console` for debugging
3. **Asset loading**: Verify file paths and Asset URL filters
4. **Performance issues**: Use theme inspector and optimize assets
5. **Changes not appearing**: Ensure development server is running and refresh browser

### Getting Help
- [Shopify Theme Documentation](https://shopify.dev/themes)
- [Shopify Community Forums](https://community.shopify.com/)
- [Shopify Partners Slack](https://shopifypartners.slack.com/)
- [Shopify CLI Documentation](https://shopify.dev/docs/themes/tools/cli)

## Next Steps

1. **Learn Advanced Liquid**: Master loops, filters, and complex logic
2. **Study Shopify APIs**: Integrate with Storefront and Admin APIs
3. **Explore App Integrations**: Connect themes with Shopify apps
4. **Build Theme Components**: Create reusable sections and blocks
5. **Optimize for Conversions**: Focus on user experience and sales

---

*This guide provides a complete workflow for Shopify theme development as a partner. Always refer to the latest Shopify documentation for updates and new features.*