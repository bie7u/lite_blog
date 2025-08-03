import React from 'react';
import { Link } from 'react-router-dom';
import { mockArticles } from '../../data/mockData';

const Home: React.FC = () => {
  return (
    <div className="articles">
      <h1 className="article-overview-category">
        Latest Articles
      </h1>

      <div className="articles-content">
        {mockArticles.map((article) => (
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
        ))}
      </div>
    </div>
  );
};

export default Home;