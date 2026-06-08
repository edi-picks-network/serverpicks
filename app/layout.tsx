import type { Metadata } from "next";
import "./globals.css";
import CookieBanner from "./components/CookieBanner";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Server Picks — Honest Hosting Reviews & Comparisons",
  description:
    "Compare top cloud hosting and VPS providers with verified reviews, pricing breakdowns, and expert comparisons. Find the perfect hosting platform for your business needs. Trusted by developers worldwide.",
  keywords: [
    "cloud hosting",
    "VPS hosting",
    "dedicated servers",
    "web hosting comparison",
    "cloud providers",
  ],
  verification: {
    google: "T5bb4mZivi0CfaYYRiKZLSNIWmhvAX6_RVgDEyonTGo",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="font-sans bg-white text-gray-900 antialiased min-h-screen flex flex-col">
        <header className="border-b border-gray-100 bg-white/80 backdrop-blur-sm sticky top-0 z-50">
          <div className="max-w-6xl mx-auto px-6 h-14 flex items-center justify-between">
            <Link href="/" className="font-bold text-gray-900 text-lg">
              Server Picks
            </Link>
            <nav className="flex items-center gap-6 text-sm text-gray-500">
              <Link href="/all-tools" className="hover:text-blue-700 transition-colors">Providers</Link>
              <Link href="/blog" className="hover:text-blue-700 transition-colors">Articles</Link>
              <Link href="/about" className="hover:text-blue-700 transition-colors">About</Link>
            </nav>
          </div>
        </header>

        <main className="flex-1">{children}</main>

        <footer className="bg-gray-900 text-gray-400 py-10">
          <div className="max-w-6xl mx-auto px-6">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 mb-8">
              <div>
                <h4 className="text-white font-semibold mb-3">Server Picks</h4>
                <p className="text-sm leading-relaxed">Independent hosting comparisons for developers and businesses.</p>
              </div>
              <div>
                <h4 className="text-white font-semibold mb-3">Explore</h4>
                <ul className="space-y-2 text-sm">
                  <li><Link href="/all-tools" className="hover:text-white transition-colors">All Providers</Link></li>
                  <li><Link href="/blog" className="hover:text-white transition-colors">Articles</Link></li>
                  <li><Link href="/about" className="hover:text-white transition-colors">About</Link></li>
                </ul>
              </div>
              <div>
                <h4 className="text-white font-semibold mb-3">Categories</h4>
                <ul className="space-y-2 text-sm">
                  <li><Link href="/faq" className="hover:text-white transition-colors">FAQ</Link></li>
                </ul>
              </div>
              <div>
                <h4 className="text-white font-semibold mb-3">Legal</h4>
                <ul className="space-y-2 text-sm">
                  <li><Link href="/privacy" className="hover:text-white transition-colors">Privacy</Link></li>
                  <li><Link href="/terms" className="hover:text-white transition-colors">Terms</Link></li>
                  <li><Link href="/disclosure" className="hover:text-white transition-colors">Disclosure</Link></li>
                </ul>
              </div>
            </div>
            <div className="pt-8 border-t border-gray-800 text-center text-sm">
              © {new Date().getFullYear()} Server Picks. All rights reserved.
            </div>
          </div>
        </footer>

        <CookieBanner />
      </body>
    </html>
  );
}
