export default function Signup() {
    return (
  
      
      <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white">
  
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
          <a href="./" className="text-gray-400 hover:text-white underline">
            Information
          </a>
        </div>
      </header>

  
  
        <h1 className="text-4xl font-bold mb-8">Welcome back 👋</h1>
        <form className="flex flex-col space-y-4 w-80">
          <input
            type="email"
            placeholder="Email Address"
            className="px-4 py-2 rounded bg-gray-800 text-white border border-gray-600"
          />
          <input
            type="password"
            placeholder="Password"
            className="px-4 py-2 rounded bg-gray-800 text-white border border-gray-600"
          />
          <button
            type="submit"
            className="px-4 py-2 bg-black rounded-lg text-white font-semibold hover:bg-gray-700"
          >
            Login
          </button>
        </form>

        {/* Footer */}
        <footer className="absolute bottom-6 text-center">
          <p style={{ marginBottom: "0px" }} className="text-sm text-gray-400 mb-2">
            Created by Bhav Grewal, Karolina Dubiel, Kevin Li, and Zachary Levesque for Hack the North 2024.
          </p>
          <a href="#" style={{ marginBottom: "20px" }} className="text-sm text-gray-400 hover:text-white underline">
            Project Information →
          </a>
        </footer>
      </div>
    );
  }
  