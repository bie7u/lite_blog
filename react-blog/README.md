# React Lite Blog

A modern React-based Single Page Application (SPA) migrated from Django. This blog application features a responsive design, smooth navigation, and a clean user interface.

## Features

- ✅ **React SPA with TypeScript**: Built with Vite for fast development and optimized builds
- ✅ **React Router**: Client-side routing with support for articles and categories
- ✅ **Responsive Design**: Mobile-first approach with hamburger menu for mobile devices
- ✅ **Desktop Sidebar**: Beautiful sidebar navigation with profile and social links on desktop
- ✅ **Article Management**: Browse articles by category or view individual article details
- ✅ **Modern Styling**: Migrated CSS from original Django application with modern best practices
- ✅ **Accessibility**: Proper ARIA labels and semantic HTML structure
- ✅ **Fast Performance**: Optimized build with Vite and modern JavaScript

## Screenshots

### Mobile View
![Mobile Home](https://github.com/user-attachments/assets/e0361b02-e49f-4a05-b7d1-250e01230a3e)

### Mobile Menu
![Mobile Menu](https://github.com/user-attachments/assets/ec483b29-56b8-43cf-85cc-a7060c3af733)

### Article Detail
![Article Detail](https://github.com/user-attachments/assets/d1faaf4a-4d18-4d2c-b9d4-b1bf91153555)

### Desktop View
![Desktop Home](https://github.com/user-attachments/assets/61b241f6-e987-4f55-a9c8-e6d798d2499f)

![Desktop Category](https://github.com/user-attachments/assets/167c4ba1-6935-42f8-9e86-ad666bfb8030)

## Technology Stack

- **Frontend Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **Routing**: React Router DOM
- **Styling**: CSS with responsive design
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Roboto)

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm or yarn

### Installation

1. Navigate to the React application directory:
   ```bash
   cd react-blog
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser and visit `http://localhost:5173`

### Build for Production

```bash
npm run build
```

The built files will be in the `dist` directory.

### Preview Production Build

```bash
npm run preview
```

## Project Structure

```
react-blog/
├── public/                 # Static assets
│   ├── images.jpeg        # Profile image
│   └── landscape2.jpg     # Background image
├── src/
│   ├── components/        # React components
│   │   ├── Layout/        # Main layout component
│   │   ├── Navbar/        # Desktop sidebar navigation
│   │   ├── MobileNavbar/  # Mobile hamburger menu
│   │   └── Footer/        # Footer component
│   ├── pages/             # Page components
│   │   ├── Home/          # Homepage with article list
│   │   ├── ArticleDetail/ # Individual article view
│   │   └── Category/      # Category-filtered articles
│   ├── data/              # Mock data and types
│   ├── App.tsx            # Main App component with routing
│   ├── main.tsx           # Application entry point
│   └── index.css          # Global styles
├── package.json
└── README.md
```

## Features Migrated from Django

### ✅ Completed Migration

1. **Layout Structure**: Converted Django base template to React Layout component
2. **Navigation**: 
   - Desktop sidebar with profile, social links, and navigation menu
   - Mobile hamburger menu with smooth animations
3. **Routing**: Replaced HTMX with React Router for SPA navigation
4. **Styling**: Migrated all CSS styles to React-compatible format
5. **Responsive Design**: Preserved mobile-first responsive behavior
6. **Article Display**: 
   - Homepage with latest articles
   - Article detail pages with rich content
   - Category filtering
7. **Interactive Elements**: Converted JavaScript hamburger menu to React hooks
8. **Accessibility**: Maintained ARIA labels and semantic HTML

### 📝 Mock Data

Since this is a frontend-only migration, the application uses mock data stored in `src/data/mockData.ts`. In a real-world scenario, you would:

1. **Create a REST API** to replace the Django backend
2. **Use React Query or SWR** for data fetching and caching
3. **Add a CMS integration** (like Strapi, Contentful, or Sanity)
4. **Implement search functionality**
5. **Add user authentication** if needed

## Customization

### Adding New Articles

Edit `src/data/mockData.ts` to add new articles or categories.

### Styling

The main styles are in `src/index.css`. The application uses a responsive design that automatically switches between mobile and desktop layouts at 1300px breakpoint.

### Social Links

Update the social media links in `src/components/Navbar/Navbar.tsx`.

## Browser Support

- Chrome (latest)
- Firefox (latest)  
- Safari (latest)
- Edge (latest)

## License

MIT License

## Original Django Version

This React application was migrated from a Django-based blog. The original functionality and design have been preserved while modernizing the technology stack for better performance and maintainability.