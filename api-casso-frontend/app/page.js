import Image from "next/image";
import styles from './dashboard/layout.module.css';

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-gray-900 via-gray-800 to-black text-white font-sans">

    {/* Top Header */}
   <header className="flex max-w-screen-xl mx-auto justify-between items-center w-full p-4 text-white fixed top-5 z-10">
        {/* Left: APIcasso */}
        <div style={{opacity: "50%"}} className="text-2xl font-bold">
          <a href="./">APIcasso</a>
        </div>

        {/* Right: Dashboard and Log out links side by side */}
        <div className="flex space-x-4">
          <a href="/dashboard" className="text-gray-400 hover:text-white underline">
            Dashboard
          </a>
          <a href="/info" className="text-gray-400 hover:text-white underline">
            Information
          </a>
        </div>
      </header>

  
      
      {/* Main Section */}
      <div className="flex flex-col items-center justify-center">
        <h1 style={{ marginTop: "-100px" }}  className="text-6xl font-bold text-center mb-8">
          Turn any website into a <br /> well-defined API 🎨
        </h1>
        
        {/* Get Started Button */}
    <a href="/signup">
    <button style={{marginTop: 0 + 'em'}} className={styles.createButton}>
          Get started <span className={styles.arrow}>→</span>
        </button>
      </a>

        {/* Login Link */}
        <p>
          Already have an account?{' '}
          <a href="/login" className="text-gray-400 hover:text-white underline">
            Log in →
          </a>
        </p>
      </div>

      {/* Footer */}
      <footer className="absolute bottom-6 text-center">
        <p className="text-sm text-gray-400 mb-2">
          Created by Bhav Grewal, Karolina Dubiel, Kevin Li, and Zachary Levesque for Hack the North 2024.
        </p>
        <a href="/info" className="text-sm text-gray-400 hover:text-white underline">
          Project Information →
        </a>
      </footer>
    </div>
  )
}
