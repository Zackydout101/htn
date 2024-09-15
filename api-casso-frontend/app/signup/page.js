"use client";
import React, { useState } from "react";
import { navigate } from "./server";

export default function Signup() {
  const [state, setState] = useState({ email: "", password: "", name: "" });

  const handleInfo = (e) => {
    const { name, value } = e.target;
    setState((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSignUp = (e) => {
    e.preventDefault();
    console.log("User signed up with the following details:", state);

    fetch("http://127.0.0.1:5000/auth/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ password: state.password, email: state.email }),
    })
      .then((response) => {
        console.log(response);
        if (response.status === 200) {
          navigate("/dashboard");
        }
      })
      .catch((error) => console.error("Error:", error));
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white">
      {/* Top Header */}
      <header className="flex max-w-screen-xl mx-auto justify-between items-center w-full p-4 text-white fixed top-5 z-10">
        {/* Left: APIcasso */}
        <div style={{ opacity: "50%" }} className="text-2xl font-bold">
          <a href="./">APIcasso</a>
        </div>
        {/* Right: Dashboard and Log out links side by side */}
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

      <h1 style={{ marginTop: "-100px" }} className="text-4xl font-bold mb-8">
        Create an account ⬇️
      </h1>
      <form
        onSubmit={handleSignUp}
        id="signUpForm"
        className="flex flex-col space-y-4 w-80"
      >
        <input
          type="text"
          placeholder="Full Name"
          id="name"
          name="name"
          onChange={handleInfo}
          value={state.name}
          className="px-4 py-2 rounded bg-gray-800 text-white border border-gray-600"
        />
        <input
          type="email"
          id="email"
          name="email"
          placeholder="Email Address"
          onChange={handleInfo}
          value={state.email}
          className="px-4 py-2 rounded bg-gray-800 text-white border border-gray-600"
        />
        <input
          id="password"
          name="password"
          type="password"
          onChange={handleInfo}
          value={state.password}
          placeholder="Password"
          className="px-4 py-2 rounded bg-gray-800 text-white border border-gray-600"
        />
        <button
          type="submit"
          className="px-4 py-2 bg-black rounded-lg text-white font-semibold hover:bg-gray-700"
        >
          Sign Up
        </button>
      </form>

      {/* Footer */}
      <footer className="w-full p-4 fixed bottom-0 left-0 justify-center items-center text-center text-white bg-gradient-to-b from-transparent via-gray-900 to-black">
        <p
          style={{ marginBottom: "0px" }}
          className="text-sm text-gray-400 mb-2"
        >
          Created by Bhav Grewal, Karolina Dubiel, Kevin Li, and Zachary
          Levesque for Hack the North 2024.
        </p>
        <a
          href="/info"
          style={{ marginBottom: "20px" }}
          className="text-sm text-gray-400 hover:text-white underline"
        >
          Project Information →
        </a>
      </footer>
    </div>
  );
}
