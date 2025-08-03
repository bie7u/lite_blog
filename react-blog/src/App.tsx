import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout/Layout';
import Home from './pages/Home/Home';
import ArticleDetail from './pages/ArticleDetail/ArticleDetail';
import Category from './pages/Category/Category';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="article/:id" element={<ArticleDetail />} />
          <Route path="category/:id" element={<Category />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
