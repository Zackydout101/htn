export default function Signup() {
  return (

    
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white">

      {/* Top Header */}


      <h1 className="text-4xl font-bold mb-8">Create Your Account</h1>
      <form className="flex flex-col space-y-4 w-80">
        <input
          type="text"
          placeholder="Full Name"
          className="px-4 py-2 rounded bg-gray-800 text-white border border-gray-600"
        />
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
          Sign Up
        </button>
      </form>
    </div>
  );
}
