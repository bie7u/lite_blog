export interface Article {
  id: number;
  title: string;
  description: string;
  content: string;
  created_at: string;
  category: string;
}

export interface Category {
  id: number;
  name: string;
}

export const mockCategories: Category[] = [
  { id: 1, name: "Technology" },
  { id: 2, name: "Programming" },
  { id: 3, name: "Web Development" },
  { id: 4, name: "React" },
];

export const mockArticles: Article[] = [
  {
    id: 1,
    title: "Getting Started with React",
    description: "Learn the basics of React and how to build your first component",
    content: `
      <h2>Introduction to React</h2>
      <p>React is a powerful JavaScript library for building user interfaces. In this article, we'll explore the fundamentals of React and learn how to create your first component.</p>
      
      <h3>What is React?</h3>
      <p>React is a declarative, efficient, and flexible JavaScript library for building user interfaces. It lets you compose complex UIs from small and isolated pieces of code called "components".</p>
      
      <h3>Your First Component</h3>
      <p>Here's how to create a simple React component:</p>
      
      <pre><code>
function Welcome(props) {
  return &lt;h1&gt;Hello, {props.name}&lt;/h1&gt;;
}
      </code></pre>
      
      <p>This component accepts a "props" object and returns a React element. You can use this component throughout your application.</p>
      
      <h3>Conclusion</h3>
      <p>React makes it painless to create interactive UIs. Give it a try and see how it can transform your web development experience!</p>
    `,
    created_at: "2024-01-15",
    category: "React"
  },
  {
    id: 2,
    title: "Modern JavaScript Features",
    description: "Explore the latest JavaScript features that every developer should know",
    content: `
      <h2>Modern JavaScript: ES6 and Beyond</h2>
      <p>JavaScript has evolved significantly over the years. Let's explore some modern features that can make your code cleaner and more efficient.</p>
      
      <h3>Arrow Functions</h3>
      <p>Arrow functions provide a more concise way to write functions:</p>
      
      <pre><code>
// Traditional function
function add(a, b) {
  return a + b;
}

// Arrow function
const add = (a, b) => a + b;
      </code></pre>
      
      <h3>Destructuring</h3>
      <p>Extract values from arrays or objects:</p>
      
      <pre><code>
const person = { name: 'John', age: 30 };
const { name, age } = person;
      </code></pre>
      
      <h3>Template Literals</h3>
      <p>Create strings with embedded expressions:</p>
      
      <pre><code>
const message = \`Hello, \${name}! You are \${age} years old.\`;
      </code></pre>
    `,
    created_at: "2024-01-10",
    category: "Programming"
  },
  {
    id: 3,
    title: "CSS Grid vs Flexbox",
    description: "Understanding when to use CSS Grid and when to use Flexbox",
    content: `
      <h2>CSS Grid vs Flexbox: Choosing the Right Tool</h2>
      <p>Both CSS Grid and Flexbox are powerful layout systems, but they serve different purposes. Let's understand when to use each.</p>
      
      <h3>Flexbox</h3>
      <p>Flexbox is designed for one-dimensional layouts. It's perfect for:</p>
      <ul>
        <li>Navigation bars</li>
        <li>Centering content</li>
        <li>Distributing space between items</li>
      </ul>
      
      <h3>CSS Grid</h3>
      <p>CSS Grid is designed for two-dimensional layouts. It excels at:</p>
      <ul>
        <li>Page layouts</li>
        <li>Complex grid systems</li>
        <li>Overlapping elements</li>
      </ul>
      
      <h3>Conclusion</h3>
      <p>Use Flexbox for components and CSS Grid for layouts. They work great together!</p>
    `,
    created_at: "2024-01-05",
    category: "Web Development"
  },
  {
    id: 4,
    title: "The Future of Web Development",
    description: "Exploring emerging trends and technologies shaping the web",
    content: `
      <h2>The Future of Web Development</h2>
      <p>Web development is constantly evolving. Let's look at some trends that are shaping the future of web development.</p>
      
      <h3>WebAssembly</h3>
      <p>WebAssembly (WASM) allows you to run code written in other languages at near-native speed in the browser.</p>
      
      <h3>Progressive Web Apps</h3>
      <p>PWAs bridge the gap between web and mobile apps, offering native-like experiences on the web.</p>
      
      <h3>Serverless Architecture</h3>
      <p>Serverless computing allows developers to focus on code without managing servers.</p>
      
      <h3>AI Integration</h3>
      <p>Machine learning and AI are becoming more accessible to web developers through APIs and libraries.</p>
    `,
    created_at: "2023-12-28",
    category: "Technology"
  }
];