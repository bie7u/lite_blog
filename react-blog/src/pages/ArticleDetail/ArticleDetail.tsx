import React from 'react';
import { useParams, Navigate } from 'react-router-dom';
import { mockArticles } from '../../data/mockData';

const ArticleDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const articleId = id ? parseInt(id, 10) : null;
  
  const article = articleId ? mockArticles.find(a => a.id === articleId) : null;

  if (!article) {
    return <Navigate to="/" replace />;
  }

  return (
    <div className="main-content">
      <div className="article">
        <div className="header">
          <h1 className="header-title-text">{article.title}</h1>
          <span className="article-date-overview">
            Publication Date: {article.created_at}
          </span>
          <p><strong>Category:</strong> {article.category}</p>
        </div>
        
        <div 
          dangerouslySetInnerHTML={{ __html: article.content }}
          style={{ marginTop: '2rem' }}
        />
      </div>
    </div>
  );
};

export default ArticleDetail;