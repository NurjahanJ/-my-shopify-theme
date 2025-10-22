# Modern Stitch Fiber - Shopify Theme

A custom Shopify theme for Modern Stitch Fiber store, built on the Horizon theme foundation.

## 🚀 Development Setup

### Prerequisites
- [Shopify CLI](https://shopify.dev/docs/themes/tools/cli) installed
- Node.js and npm
- Git
- Shopify Partner account with access to the development store

### Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd my-shopify-theme
   ```

2. **Authenticate with Shopify**
   ```bash
   shopify auth login
   ```

3. **Start development server**
   ```bash
   shopify theme dev --store modern-stitch-fiber.myshopify.com
   ```

4. **Pull latest theme changes** (if needed)
   ```bash
   shopify theme pull --store modern-stitch-fiber.myshopify.com --theme 181391360298
   ```

## 📁 Theme Structure

```
├── assets/           # CSS, JS, images, fonts
├── blocks/           # Theme blocks (Shopify 2.0)
├── config/           # Theme settings and data
├── layout/           # Base templates (theme.liquid)
├── locales/          # Translation files
├── sections/         # Reusable content blocks
├── snippets/         # Reusable code fragments
├── templates/        # Page templates
└── guide.md          # Development guide
```

## 🎨 Theme Features

- **Modern Design**: Clean, professional aesthetic
- **Shopify 2.0 Compatible**: Uses sections and blocks architecture
- **Responsive**: Mobile-first design approach
- **Customizable**: Multiple color schemes and typography options
- **Performance Optimized**: Fast loading and SEO friendly

## 🛠️ Development Workflow

1. **Make changes** to theme files locally
2. **Test changes** using the development server
3. **Commit changes** to Git
4. **Push to repository** for version control
5. **Deploy to store** when ready

## 📋 Available Commands

```bash
# Development
shopify theme dev --store modern-stitch-fiber.myshopify.com

# Pull theme from store
shopify theme pull --store modern-stitch-fiber.myshopify.com --theme 181391360298

# Push theme to store
shopify theme push --store modern-stitch-fiber.myshopify.com

# Check theme for issues
shopify theme check

# Share development theme
shopify theme share --store modern-stitch-fiber.myshopify.com
```

## 🎯 Store Information

- **Store URL**: modern-stitch-fiber.myshopify.com
- **Theme**: Horizon (#181391360298)
- **Framework**: Shopify Liquid + Shopify 2.0

## 📚 Resources

- [Shopify Theme Development Guide](./guide.md)
- [Shopify Liquid Documentation](https://shopify.dev/docs/themes/liquid)
- [Shopify CLI Documentation](https://shopify.dev/docs/themes/tools/cli)

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

---

