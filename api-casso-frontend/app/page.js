import Image from "next/image";


export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-gray-900 via-gray-800 to-black text-white font-sans">
      {/* Main Section */}
      <div className="flex flex-col items-center justify-center">
        <h1 className="text-6xl font-bold text-center mb-8">
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
          Already have an account?{' '}
          <a href="#" className="text-gray-400 hover:text-white underline">
            Log in →
          </a>
        </p>
      </div>

      {/* Footer */}
      <footer className="absolute bottom-6 text-center">
        <p className="text-sm text-gray-400 mb-2">
          Created by Bhav Grewal, Karolina Dubiel, Kevin Li, and Zachary Levesque for Hack the North 2024.
        </p>
        <a href="#" className="text-gray-400 hover:text-white underline">
          Project Information →
        </a>
      </footer>
    </div>
  )
}
