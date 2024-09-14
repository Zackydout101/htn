"use client";
import React, { useEffect, useState } from "react";
import styles from "./layout.module.css"; // Assuming you have layout.css for global styles

const Layout = () => {
  const [key, setKey] = useState("");  // State for the API key input
  const [schema, setSchema] = useState("");  // State for the schema/keywords input
  const [boxes, setBoxes] = useState([]);  // State to store API boxes
  const [data, setData] = useState("");  // State for API data

  // Handle input changes for API key
  const handleKeyChange = (event) => {
    setKey(event.target.value);
  };

  // Handle input changes for schema/keywords
  const handleSchemaChange = (event) => {
    setSchema(event.target.value);
  };

  // Handle adding new box when submit button is clicked
  const handleSubmit = () => {
    if (key.trim() !== "" && schema.trim() !== "") {
      setBoxes((prevBoxes) => [...prevBoxes, { key, schema }]);
      setKey("");  // Clear API key input after adding
      setSchema("");  // Clear schema input after adding
    }
  };

  // Handle navigation when sidebar buttons are clicked
  const handleNavigation = (route) => {
    window.location.href = route;  // Navigate to new page
  };

  // Fetch data from the API on component mount
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("/api/hello?key=hola");
      const result = await response.json();
      setData(result.value);
    };
    fetchData();
  }, []);

  return (
    <div className={styles.container}>
      {/* Header Section */}
      <header className={styles.header}>
        <div className={styles.headerContent}>
          <h1 className={styles.title}>My APIs</h1>
          <p className={styles.description}>
            Details for all APIs created on APIcasso.
          </p>

          {/* Inline fields for API key and Schema */}
          <div className={styles.inputWrapper}>
            <input
              type="text"
              value={key}
              onChange={handleKeyChange}
              placeholder="Enter URL"
              className={styles.inputField}  // Assuming you have styling for the input field
            />
            <input
              type="text"
              value={schema}
              onChange={handleSchemaChange}
              placeholder="Enter Schema/Keywords"
              className={styles.inputField}  // Assuming you have styling for the input field
              style={{ marginLeft: "10px" }}  // Inline spacing between the two fields
            />

            {/* Create new box button */}
            <button
              style={{ marginLeft: "650px", marginTop: "10px", width: "60%"}}
              className={styles.createButton}
              onClick={handleSubmit}
            >
              Create new <span className={styles.arrow}>→</span>
            </button>
          </div>
        </div>

        {/* Grid Section for displaying API boxes */}
        <div className={styles.gridContainer}>
          {boxes.map((box, index) => (
            <div key={index} className={styles.apiBox}>
              <p className={styles.apiDetail}>
                <strong>URL:</strong> {box.key}  {/* Display the entered key */}
              </p>
              <p className={styles.apiDetail}>
                <strong>Schema/Keywords:</strong> {box.schema}  {/* Display the schema/keywords */}
              </p>
            </div>
          ))}
        </div>
      </header>

      {/* Main Content Section */}
      <main className={styles.mainContent}>
        {/* Render dynamic content */}
      </main>

      {/* Footer */}
      
      <footer className="absolute bottom-6">
        <p style={{ marginBottom: "0px" }}  className="text-sm text-gray-400 mb-2">
          Created by Bhav Grewal, Karolina Dubiel, Kevin Li, and Zachary Levesque for Hack the North 2024.
        </p>
        <a href="#" style={{ marginBottom: "20px" }}  className="text-sm text-gray-400 hover:text-white underline">
          Project Information →
        </a>
      </footer>
      </div>
    

    
  );
};

export default Layout;
