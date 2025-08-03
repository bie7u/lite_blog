import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { mockCategories } from '../../data/mockData';

const MobileNavbar: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const closeMenu = () => {
    setIsOpen(false);
  };

  return (
    <nav className="mobile-navbar">
      <div className="mobile-nav-left">
        <p>Your Website Name</p>
      </div>

      <div>
        <button
          className={`hamburger ${isOpen ? 'active' : ''}`}
          onClick={toggleMenu}
          aria-label="Menu"
          aria-expanded={isOpen}
        >
          <span></span>
          <span></span>
          <span></span>
        </button>

        <nav className={`menu ${isOpen ? 'open' : ''}`}>
          <ul>
            <li>
              <Link 
                to="/" 
                className="mobile-nav-home" 
                onClick={closeMenu}
                style={{ 
                  color: '#fff', 
                  textDecoration: 'none',
                  fontSize: '3rem',
                  display: 'block',
                  margin: '1.5rem 0'
                }}
              >
                Home
              </Link>
            </li>
            {mockCategories.map((category, index) => (
              <li key={category.id} style={{ '--i': index + 2 } as React.CSSProperties}>
                <Link
                  to={`/category/${category.id}`}
                  className="menu-mobile-nav"
                  onClick={closeMenu}
                  style={{ 
                    color: '#fff', 
                    textDecoration: 'none',
                    fontSize: '3rem',
                    display: 'block',
                    margin: '1.5rem 0'
                  }}
                >
                  {category.name}
                </Link>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </nav>
  );
};

export default MobileNavbar;