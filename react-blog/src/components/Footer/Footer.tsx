import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="footer">
      Powered by{' '}
      <a 
        href="https://github.com/bie7u/lite_blog" 
        target="_blank" 
        rel="noopener noreferrer"
      >
        React Lite Blog
      </a>
    </footer>
  );
};

export default Footer;