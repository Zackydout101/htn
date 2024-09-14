// app/layout.tsx
"use client"
import React from 'react';
import styles from './layout.module.css'; // Import CSS module

const Layout = () => {


 
  


  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1>Dashboard</h1>



      
      </header>
      
      <nav className={styles.sidebar}>
        <ul>
          <li><button onClick={() => handleNavigation('/dashboard')}>Dashboard</button></li>
          <li><button onClick={() => handleNavigation('/profile')}>Profile</button></li>
          <li><button onClick={() => handleNavigation('/settings')}>Settings</button></li>
          <li><button onClick={() => handleNavigation('/reports')}>Reports</button></li>
          <li><button onClick={() => handleNavigation('/help')}>Help</button></li>
        </ul>
      </nav>
      <main className={styles.mainContent}>
         
      </main>
    </div>
  );
};

export default Layout;