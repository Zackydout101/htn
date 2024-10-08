import Image from "next/image";
import styles from "./dashboard/layout.module.css";
import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-gray-900 via-gray-800 to-black text-white font-sans">
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
          <a href="https://devpost.com/software/apicasso" className="text-gray-400 hover:text-white underline">
            Information
          </a>
        </div>
      </header>
      {/* Main Section */}
      <div className="flex flex-col items-center justify-center">
        <h1
          style={{ marginTop: "-100px" }}
          className="text-6xl font-bold text-center mb-8"
        >
          Turn any website into a <br /> well-defined API 🎨
        </h1>
        {/* Get Started Button */}
        <Link href="/signup">
          <button className="px-6 py-3 bg-black rounded-lg text-white font-semibold text-lg mb-4 hover:bg-gray-700 transition shadow-[0_4px_30px_rgba(256,256,256,0.3)]">
            Get started →
          </button>
        </Link>
        {/* Login Link */}
        <p>
          Already have an account?{" "}
          <Link href="/login" className="text-gray-400 hover:text-white underline">
            Log in →
          </Link>
        </p>
      </div>
      {/* Footer */}
      <footer className="w-full p-4 fixed bottom-0 left-0 justify-center items-center text-center text-white bg-gradient-to-b from-transparent via-gray-900 to-black">
        <p className="text-sm text-gray-400 mb-2">
          Created by Bhav Grewal, Karolina Dubiel, Kevin Li, and Zachary
          Levesque for Hack the North 2024.
        </p>
        <a
          href="https://devpost.com/software/apicasso"
          className="text-sm text-gray-400 hover:text-white underline"
        >
          Project Information →
        </a>
      </footer>
    </div>
  );
}
