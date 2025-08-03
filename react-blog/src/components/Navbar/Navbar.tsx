import React from 'react';
import { Link } from 'react-router-dom';
import { mockCategories } from '../../data/mockData';

const Navbar: React.FC = () => {
  return (
    <div className="sidebar">
      <div className="up-navbar">
        <div className="nav-avatar">
          <img className="circle-img" src="/images.jpeg" alt="Avatar" />
        </div>
        <div>
          <h1>Name</h1>
        </div>
        <div className="sidebar-icons">
          <a
            className="black-icon"
            href="https://linkedin.com/in/krystian-biel/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <i className="fa-brands fa-lg fa-linkedin pointer-icon"></i>
          </a>
          <a
            className="black-icon"
            href="https://github.com/bie7u"
            target="_blank"
            rel="noopener noreferrer"
          >
            <i className="fa-brands fa-lg fa-github pointer-icon"></i>
          </a>
        </div>
      </div>

      <hr className="nav-hr" />

      <ul className="nav-down">
        <li className="nav-down-li">
          <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
            Home
          </Link>
        </li>
        <hr className="nav-li-hr" />
        {mockCategories.map((category) => (
          <React.Fragment key={category.id}>
            <li className="nav-down-li">
              <Link 
                to={`/category/${category.id}`} 
                style={{ textDecoration: 'none', color: 'inherit' }}
              >
                {category.name}
              </Link>
            </li>
            <hr className="nav-li-hr" />
          </React.Fragment>
        ))}
      </ul>
    </div>
  );
};

export default Navbar;