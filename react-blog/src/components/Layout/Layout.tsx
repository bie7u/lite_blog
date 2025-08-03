import React from 'react';
import { Outlet } from 'react-router-dom';
import Navbar from '../Navbar/Navbar';
import MobileNavbar from '../MobileNavbar/MobileNavbar';
import Footer from '../Footer/Footer';

const Layout: React.FC = () => {
  return (
    <>
      {/* Mobile Navbar */}
      <MobileNavbar />

      {/* Page Layout */}
      <div className="page-layout">
        <Navbar />

        <div className="main-ar">
          <div id="main-area">
            <Outlet />
          </div>

          {/* Footer */}
          <div>
            <Footer />
          </div>
        </div>
      </div>
    </>
  );
};

export default Layout;