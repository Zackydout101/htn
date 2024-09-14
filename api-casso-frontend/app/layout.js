import localFont from "next/font/local";
import { Inter } from "next/font/google";  // Importing Inter from Google Fonts
import "./globals.css";

// Load your local fonts
const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

// Load Inter from Google Fonts
const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter", // Use CSS variable for the font
  display: "swap",  // Swap ensures text is displayed while the font is loading
});

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${inter.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
