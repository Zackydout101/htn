"use client";
import React, { useEffect, useState, useRef } from "react";
import styles from "./layout.module.css"; // Assuming you have layout.css for global styles

const Layout = () => {
  const [key, setKey] = useState(""); // State for the API key input
  const [schema, setSchema] = useState(""); // State for the schema/keywords input
  const [boxes, setBoxes] = useState([]); // State to store API boxes

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
      setKey(""); // Clear API key input after adding
      setSchema(""); // Clear schema input after adding
    }
  };

  // API Box Component with Expand/Collapse Feature
  const ApiBox = ({ url, schema }) => {
    const [isExpanded, setIsExpanded] = useState(false);
    const schemaRef = useRef(null);

    const toggleExpand = () => {
      setIsExpanded(!isExpanded);
    };

    return (
      <div className="bg-black text-white p-4 rounded-lg shadow-md mb-4 w-full">
        <p><strong>PermaURL:</strong> https://example.com/{url}</p> {/* Added PermaURL */}
        <p><strong>URL:</strong> {url}</p>
        <div
          ref={schemaRef}
          style={{
            maxHeight: isExpanded ? `${schemaRef.current.scrollHeight}px` : "80px",
            overflow: "hidden",
            transition: "max-height 0.3s ease-in-out"
          }}
        >
          <p><strong>Schema:</strong> {schema}</p>
        </div>
        <button
          onClick={toggleExpand}
          className="mt-2 text-sm text-blue-400 hover:underline"
        >
          {isExpanded ? 'Show Less' : 'Show More'}
        </button>
      </div>
    );
  };

  return (
    <div className={styles.containerspecial}>
      {/* Top Header */}
      <header
        style={{
          marginTop: "-80px",
          marginLeft: "-10px",
          marginBottom: "25px",
        }}
        className="flex justify-between items-center w-full p-4 text-white"
      >
        <div className="text-2xl font-bold">
          <a style={{ opacity: "50%" }} href="./">
            APIcasso
          </a>
        </div>

        <div className="flex space-x-4">
          <a
            href="/dashboard"
            className="text-gray-400 hover:text-white underline"
          >
            Dashboard
          </a>
          <a href="./" className="text-gray-400 hover:text-white underline">
            Information
          </a>
        </div>
      </header>

      {/* Main Section */}
      <div className={styles.mainSection}>
        <header className={styles.header}>
          <div className={styles.headerContent}>
            <h1 className={styles.title}>My schemas</h1>
            <p className={styles.description}>
              Provide a URL and an empty JSON schema. Press "Create New".
              Receive a completed one. ✅
            </p>

            <div
              className={styles.inputWrapper}
              style={{
                display: "flex",
                flexDirection: "column",
                gap: "10px",
                alignItems: "flex-start",
              }}
            >
              <input
                type="text"
                value={key}
                onChange={handleKeyChange}
                placeholder="Enter URL"
                className="w-1/2 px-4 py-2 text-base text-white bg-gray-800 border border-gray-600 rounded focus:outline-none focus:border-blue-500"
              />

              <textarea
                value={schema}
                onChange={handleSchemaChange}
                placeholder="Enter JSON Schema"
                className="w-full h-48 px-4 py-2 text-base text-white bg-gray-800 border border-gray-600 rounded focus:outline-none focus:border-blue-500 resize-none"
              />

              <button
                style={{ marginTop: "10px", marginBottom: "50px", width: "20%" }}
                className={styles.createButton}
                onClick={handleSubmit}
              >
                Create new <span className={styles.arrow}>→</span>
              </button>
            </div>
          </div>

          {/* Grid Section for displaying API boxes */}
          <div className="w-full max-w-4xl mt-8">
            {boxes.map((box, index) => (
              <ApiBox key={index} url={box.key} schema={box.schema} />
            ))}
          </div>
        </header>

        <main className={styles.mainContent}>
          {/* Render dynamic content */}
        </main>

        <footer className="w-full p-4 fixed bottom-0 left-0 justify-center items-center text-center text-white bg-gradient-to-b from-transparent via-gray-900 to-black">
          <div>
            <p className="text-sm text-gray-400 mb-2">
              Created by Bhav Grewal, Karolina Dubiel, Kevin Li, and Zachary
              Levesque for Hack the North 2024.
            </p>
            <a
              href="/info"
              className="text-sm text-gray-400 hover:text-white underline"
            >
              Project Information →
            </a>
          </div>
        </footer>
      </div>
    </div>
  );
};

export default Layout;
