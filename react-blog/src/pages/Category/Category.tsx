import React from 'react';
import { useParams, Link, Navigate } from 'react-router-dom';
import { mockArticles, mockCategories } from '../../data/mockData';

const Category: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const categoryId = id ? parseInt(id, 10) : null;
  
  const category = categoryId ? mockCategories.find(c => c.id === categoryId) : null;
  const categoryArticles = category 
    ? mockArticles.filter(article => article.category === category.name)
    : [];

  if (!category) {
    return <Navigate to="/" replace />;
  }

  return (
    <div className="articles">
      <h1 className="article-overview-category">
        {category.name}
      </h1>

      <div className="articles-content">
        {categoryArticles.length === 0 ? (
          <p>No articles found in this category.</p>
        ) : (
          categoryArticles.map((article) => (
            <div
              key={article.id}
              className="article-overview"
            >
              <Link 
                to={`/article/${article.id}`}
                style={{ textDecoration: 'none', color: 'inherit' }}
              >
                <h2 className="article-overview-title">{article.title}</h2>
                <span className="article-overview-write">
                  {article.description}...
                </span>
                <span className="article-date-overview">
                  Publication Date: {article.created_at}
                </span>
              </Link>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Category;