import type { Metadata } from "next";
import { Nunito } from "next/font/google";
import "./globals.css";
import Header from "./sections/Header";
import Footer from "./sections/Footer";
import CookieBanner from "./components/CookieBanner";

const nunito = Nunito({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  variable: "--font-nunito",
});

export const metadata: Metadata = {
  title: "Server Picks — Honest Hosting Reviews & Comparisons",
  description:
    "Compare top cloud hosting and VPS providers with verified reviews, pricing breakdowns, and expert comparisons. Find the perfect hosting platform for your business needs. Trusted by developers worldwide.",
  keywords: [
    "cloud hosting",
    "VPS hosting",
    "hosting reviews",
    "server hosting",
    "web hosting comparison",
    "dedicated server",
    "cloud providers",
    "hosting platforms",
  ],
  verification: {
    google: "T5bb4mZivi0CfaYYRiKZLSNIWmhvAX6_RVgDEyonTGo",
  },
  openGraph: {
    type: "website",
    locale: "en_US",
    siteName: "Server Picks",
    title: "Server Picks — Honest Hosting Reviews & Comparisons",
    description:
      "Compare top cloud hosting and VPS providers with verified reviews, pricing breakdowns, and expert comparisons.",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={nunito.variable}>
      <body className={`${nunito.className} min-h-screen antialiased`}>
        <div className="aurora-bg" />
        <div className="grid-pattern" />

        <Header />

        <main className="relative z-10">{children}</main>

        <Footer />

        <CookieBanner />
      </body>
    </html>
  );
}
