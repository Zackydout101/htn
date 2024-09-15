"use client";
import React, { useEffect, useState, useRef } from "react";
import styles from "./layout.module.css";

const Layout = () => {
  const [key, setKey] = useState("");
  const [api_uuid, setAPIUUID] = useState("");
  const [schema, setSchema] = useState("");
  const [boxes, setBoxes] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [loadingProgress, setLoadingProgress] = useState(0);

  const handleKeyChange = (event) => {
    setKey(event.target.value);
  };

  const handleSchemaChange = (event) => {
    setSchema(event.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("User submitted:");
    console.log("schema:", key);

    setIsLoading(true);
    setLoadingProgress(0);

    const loadingInterval = setInterval(() => {
      setLoadingProgress((prevProgress) => {
        const newProgress = prevProgress + 2; // Increase by 2% every second (50 seconds total)
        return newProgress > 100 ? 100 : newProgress;
      });
    }, 1000);

    fetch("http://127.0.0.1:5000/scrape", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ website_url: key, schema_string: schema }),
    })
      .then((response) => response.json())
      .then((data) => {
        clearInterval(loadingInterval);
        setIsLoading(false);
        setLoadingProgress(100);
        setAPIUUID(data.api_endpoint);
        if (key.trim() !== "" && schema.trim() !== "") {
          setBoxes((prevBoxes) => [...prevBoxes, { key, schema, api_endpoint: data.api_endpoint }]);
          setKey("");
          setSchema("");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        clearInterval(loadingInterval);
        setIsLoading(false);
        setLoadingProgress(0);
      });
  };

  const ApiBox = ({ url, schema, api_endpoint }) => {
    const [isExpanded, setIsExpanded] = useState(false);
    const schemaRef = useRef(null);
    const [isCopied, setIsCopied] = useState(false);

    const toggleExpand = () => {
      setIsExpanded(!isExpanded);
    };

    const copyToClipboard = () => {
      navigator.clipboard
        .writeText(`http://127.0.0.1:5000${api_endpoint}`)
        .then(() => {
          setIsCopied(true);
          setTimeout(() => setIsCopied(false), 1500);
        })
        .catch((err) => console.error("Failed to copy!", err));
    };

    return (
      <div className="bg-black text-white p-4 rounded-lg shadow-md mb-4 w-full">
        <div className="flex items-center">
          <p>
            <strong>PermaURL:</strong> http://127.0.0.1:5000/{api_endpoint}
          </p>
          <button
            onClick={copyToClipboard}
            className="ml-2 text-sm text-blue-400 hover:underline bg-transparent border-none cursor-pointer"
          >
            {isCopied ? "Copied!" : "Copy"}
          </button>
        </div>
        <p>
          <strong>URL:</strong> {url}
        </p>
        <div
          ref={schemaRef}
          style={{
            maxHeight: isExpanded
              ? `${schemaRef.current.scrollHeight}px`
              : "80px",
            overflow: "hidden",
            transition: "max-height 0.3s ease-in-out",
          }}
        >
          <p>
            <strong>Schema:</strong> {schema}
          </p>
        </div>
        <button
          onClick={toggleExpand}
          className="mt-2 text-sm text-blue-400 hover:underline"
        >
          {isExpanded ? "Show Less" : "Show More"}
        </button>
      </div>
    );
  };

  return (
    <div className={styles.containerspecial}>
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
                style={{
                  marginTop: "10px",
                  marginBottom: "10px",
                  width: "20%",
                }}
                className={styles.createButton}
                onClick={handleSubmit}
                disabled={isLoading}
              >
                {isLoading ? "Loading..." : "Create new"} <span className={styles.arrow}>→</span>
              </button>

              {isLoading && (
                <div className="w-full bg-gray-800 rounded-full h-2.5 mt-4">
                  <div
                    className="bg-white h-2.5 rounded-full"
                    style={{ width: `${loadingProgress}%` }}
                  ></div>
                </div>
              )}
            </div>
          </div>

          <div className="w-full max-w-4xl mt-8">
            {boxes.map((box, index) => (
              <ApiBox key={index} url={box.key} schema={box.schema} api_endpoint={box.api_endpoint} />
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
