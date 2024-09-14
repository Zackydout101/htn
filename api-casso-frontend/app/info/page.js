export default function Info() {
    return (
  
      
        <div className="relative min-h-screen flex flex-col items-center justify-center text-white">
        {/* Background Image with Overlay */}
        <div className="absolute inset-0 bg-[url('IMG_7237.jpg')] bg-cover bg-no-repeat z-0">
          <div className="absolute inset-0 bg-black opacity-50 z-0"></div> {/* Dark overlay */}
        </div>
  
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

      <div class="overflow-x-auto">
  <table class="min-w-full table-auto border-collapse border border-gray-700">
    <thead>
      <tr class="bg-gray-800 text-white">
        <th class="px-4 py-2 border border-gray-700">Name</th>
        <th class="px-4 py-2 border border-gray-700">Role</th>
      </tr>
    </thead>
    <tbody>
      <tr class="bg-gray-900 text-gray-300">
        <td class="px-4 py-2 border border-gray-700">Bhav Grewal</td>
        <td class="px-4 py-2 border border-gray-700"><li>Backend architecture</li><li>Fullstack integration with Flask</li></td>
      </tr>
      <tr class="bg-gray-800 text-gray-300">
        <td class="px-4 py-2 border border-gray-700">Karolina Dubiel</td>
        <td class="px-4 py-2 border border-gray-700"><li>Frontend development in next.js and Tailwind CSS</li><li>Dashboard UI configuration</li></td>
      </tr>
      <tr class="bg-gray-900 text-gray-300">
        <td class="px-4 py-2 border border-gray-700">Kevin Li</td>
        <td class="px-4 py-2 border border-gray-700"><li>Backend architecture</li><li>Fullstack integration with Flask</li></td>
      </tr>
      <tr class="bg-gray-800 text-gray-300">
        <td class="px-4 py-2 border border-gray-700">Zachary Levesque</td>
        <td class="px-4 py-2 border border-gray-700"><li>Crypto integration with ETH</li><li>Dashboard configuration in <code>redis</code></li></td>
      </tr>
    </tbody>
  </table>
</div>



  
  
        
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
  