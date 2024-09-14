"use client";
import React, { useState } from "react";
import { navigate } from "./server";

export default function Signup() {
  const [state, setState] = useState({ email: "", password: "", name: "" });

  const handleInfo = (e) => {
    const value = e.target.value;
    setState({
      ...state,
      [e.target.name]: value,
    });
    console.log("Name:", state);
  };

  const handleSignUp = (e) => {
    e.preventDefault();
    console.log("User signed up with the following details:");
    console.log("Name:", state);

    fetch("http://127.0.0.1:5000/auth/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ password: state.password, email: state.email }),
    })
      .then((response) => {
        console.log(response);
        if (response.status == 200) {
          navigate("/dashboard");
        }
      })
      .catch((error) => console.error("Error:", error));
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white">
      <h1 className="text-4xl font-bold mb-8">Create Your Account</h1>
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
    </div>
  );
}
