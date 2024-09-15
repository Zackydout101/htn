"use client";
import React, { useState } from "react";
import { navigate } from "../signup/server";

export default function Login() {
  const [state, setState] = useState({ email: "", password: "" });

  const handleInfo = (e) => {
    const { name, value } = e.target;
    setState((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSignIn = (e) => {
    e.preventDefault();
    console.log("User logged in with the following details:", state);

    fetch("http://127.0.0.1:5000/auth/signin", {
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
      {/* ... existing header ... */}

      <h1 style={{ marginTop: "-100px" }} className="text-4xl font-bold mb-8">
        Welcome back 👋
      </h1>
      <form
        className="flex flex-col space-y-4 w-80"
        onSubmit={handleSignIn}
        id="signInForm"
      >
        <input
          type="email"
          name="email"
          placeholder="Email Address"
          onChange={handleInfo}
          value={state.email}
          className="px-4 py-2 rounded bg-gray-800 text-white border border-gray-600"
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleInfo}
          value={state.password}
          className="px-4 py-2 rounded bg-gray-800 text-white border border-gray-600"
        />
        <button
          type="submit"
          className="px-4 py-2 bg-black rounded-lg text-white font-semibold hover:bg-gray-700"
        >
          Login
        </button>
      </form>

      {/* Add this new paragraph for the signup link */}
      <p className="mt-4 text-sm">
        Don't have an account?{" "}
        <a href="/signup" className="text-blue-400 hover:underline">
          Sign up here
        </a>
      </p>

      {/* ... existing footer ... */}
    </div>
  );
}
