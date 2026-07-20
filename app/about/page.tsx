import type { Metadata } from "next";
import Link from "next/link";
import { Globe, MapPin, Users, Cpu, BarChart3, Shield, Layers, Compass } from "lucide-react";

export const metadata: Metadata = {
  title: "About — ServerPicks",
  description:
    "ServerPicks is a cloud infrastructure benchmarking platform. We compare and review hosting providers for modern workloads.",
};

const TEAM_HIGHLIGHTS = [
  {
    icon: Compass,
    title: "Geospatial Systems Focus",
    desc: "We specialize in infrastructure for GIS, remote sensing, spatial analytics, and location intelligence workloads — not just generic cloud hosting.",
  },
  {
    icon: BarChart3,
    title: "Rigorous Benchmarks",
    desc: "Every provider is tested with geospatial benchmark suites: GDAL/OGR processing, PostGIS query throughput, tile serving latency, and raster compute performance.",
  },
  {
    icon: Shield,
    title: "Independent Analysis",
    desc: "No sponsored rankings, no affiliate bias. Our recommendations are based on real performance data collected from our Boston-based test infrastructure.",
  },
  {
    icon: Globe,
    title: "Global Perspective",
    desc: "We test from multiple geographic vantage points to provide latency and throughput data relevant to distributed geospatial systems.",
  },
];

export default function AboutPage() {
  return (
    <div className="relative pt-32 pb-20 px-6">
      <div className="max-w-[800px] mx-auto">
        <div className="text-center mb-16">
            <span className="inline-flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-geospatial-light bg-ever-700 px-3 py-1.5 rounded-md mb-4">
              <MapPin className="w-3 h-3" />
              Boston, MA
            </span>
            <h1 className="text-3xl md:text-5xl font-extrabold text-white tracking-tight mb-6">
              Your Infrastructure{' '}
              <span className="text-geospatial-light">Benchmarking Team</span>
            </h1>
            <p className="text-lg text-ever-400 leading-relaxed max-w-2xl mx-auto">
              ServerPicks is a 7-person cloud infrastructure team based in 
              Boston, Massachusetts. We benchmark, compare, and recommend cloud hosting 
              providers for data-intensive workloads.
            </p>
        </div>

        <div className="mb-16">
          <h2 className="text-2xl font-bold text-white mb-6">Our Story</h2>
          <div className="space-y-4 text-ever-400 leading-relaxed">
            <p>
            ServerPicks started in a shared workspace in Somerville, MA. 
            Our founding team of four infrastructure engineers kept running into the same 
            problem: cloud hosting recommendations were built for web developers, not 
            for people processing satellite imagery, running real-time GIS services, 
            or ingesting LiDAR point clouds at scale.
            </p>
            <p>
              We needed to know: which cloud provider delivers the fastest GDAL raster 
              operations? Which VPS host handles PostGIS spatial joins without falling 
              over? How does object storage performance vary across providers when 
              you&apos;re serving geotiff tiles to millions of users?
            </p>
            <p>
              Nobody had answers. So we built our own benchmark infrastructure — a 
              test lab in Boston running standardized geospatial workloads against every 
              major cloud provider. Today, we&apos;ve grown to a team of seven, and we 
              publish our benchmark data openly so the geospatial community can make 
              informed infrastructure decisions.
            </p>
          </div>
        </div>

        <div className="mb-16">
          <h2 className="text-2xl font-bold text-white mb-8 text-center">
            What Makes Us Different
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {TEAM_HIGHLIGHTS.map((item) => {
              const Icon = item.icon;
              return (
                <div
                  key={item.title}
                  className="bg-ever-800 border border-ever-700 rounded-xl p-6 hover:border-geospatial/50 transition-all"
                >
                  <div className="w-12 h-12 rounded-lg bg-ever-700 flex items-center justify-center mb-4">
                    <Icon className="w-6 h-6 text-geospatial" />
                  </div>
                  <h3 className="text-lg font-bold text-white mb-2">{item.title}</h3>
                  <p className="text-sm text-ever-400 leading-relaxed">{item.desc}</p>
                </div>
              );
            })}
          </div>
        </div>

        <div className="mb-16">
          <h2 className="text-2xl font-bold text-white mb-6">The Team</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div className="bg-ever-800 border border-ever-700 rounded-xl p-5">
              <div className="flex items-center gap-3 mb-2">
                <div className="w-10 h-10 rounded-full bg-geospatial/20 flex items-center justify-center text-geospatial-light font-bold">
                  M
                </div>
                <div>
                  <p className="font-semibold text-white text-sm">Marcus Chen</p>
                  <p className="text-xs text-ever-500">Lead Geospatial Engineer</p>
                </div>
              </div>
              <p className="text-xs text-ever-400">GIS architecture, PostGIS tuning, raster pipeline design. Formerly at Planet Labs.</p>
            </div>
            <div className="bg-ever-800 border border-ever-700 rounded-xl p-5">
              <div className="flex items-center gap-3 mb-2">
                <div className="w-10 h-10 rounded-full bg-geospatial/20 flex items-center justify-center text-geospatial-light font-bold">
                  A
                </div>
                <div>
                  <p className="font-semibold text-white text-sm">Aisha Patel</p>
                  <p className="text-xs text-ever-500">Cloud Infrastructure Lead</p>
                </div>
              </div>
              <p className="text-xs text-ever-400">Multi-cloud benchmarking, network latency analysis, cost optimization. Ex-AWS infrastructure team.</p>
            </div>
            <div className="bg-ever-800 border border-ever-700 rounded-xl p-5">
              <div className="flex items-center gap-3 mb-2">
                <div className="w-10 h-10 rounded-full bg-geospatial/20 flex items-center justify-center text-geospatial-light font-bold">
                  J
                </div>
                <div>
                  <p className="font-semibold text-white text-sm">James Mitchell</p>
                  <p className="text-xs text-ever-500">DevOps & Automation</p>
                </div>
              </div>
              <p className="text-xs text-ever-400">CI/CD pipelines, infrastructure as code, automated benchmark harnesses. Kubernetes specialist.</p>
            </div>
            <div className="bg-ever-800 border border-ever-700 rounded-xl p-5">
              <div className="flex items-center gap-3 mb-2">
                <div className="w-10 h-10 rounded-full bg-geospatial/20 flex items-center justify-center text-geospatial-light font-bold">
                  S
                </div>
                <div>
                  <p className="font-semibold text-white text-sm">Sarah Chen</p>
                  <p className="text-xs text-ever-500">Data Scientist & Analyst</p>
                </div>
              </div>
              <p className="text-xs text-ever-400">Performance data analysis, statistical modeling, benchmark methodology. PhD in Geospatial Science.</p>
            </div>
          </div>
        </div>

        <div className="mb-16">
          <h2 className="text-2xl font-bold text-white mb-6">Our Benchmark Methodology</h2>
          <div className="space-y-4 text-ever-400 leading-relaxed">
            <p>
              Every provider we review is tested against a standardized geospatial benchmark suite running from our Boston-based test infrastructure:
            </p>
            <ul className="list-disc pl-6 space-y-2 text-sm">
              <li>
                <strong className="text-white">GDAL/OGR Performance</strong> — raster and vector processing throughput using real-world datasets (Sentinel-2 imagery, OpenStreetMap extracts)
              </li>
              <li>
                <strong className="text-white">PostGIS Query Throughput</strong> — spatial join performance, index scan speeds, and concurrent query handling
              </li>
              <li>
                <strong className="text-white">Tile Serving Latency</strong> — MBTiles, PMTiles, and S3-based tile serving response times from multiple geographic regions
              </li>
              <li>
                <strong className="text-white">Object Storage Geo-Performance</strong> — S3-compatible storage read/write throughput for geospatial data formats
              </li>
              <li>
                <strong className="text-white">Cost-per-Benchmark</strong> — dollar cost to complete standardized geospatial processing tasks
              </li>
            </ul>
            <p className="text-sm mt-4">
              We update our benchmarks quarterly. Pricing and features change frequently,
              so we encourage verifying details directly with providers before making 
              purchasing decisions. Links to official websites are provided on every provider page.
            </p>
          </div>
        </div>

        {/* CTA */}
        <div className="text-center bg-ever-800 border border-ever-700 rounded-xl p-10">
          <h2 className="text-2xl font-bold text-white mb-4">
            Have a suggestion?
          </h2>
          <p className="text-ever-400 mb-6 max-w-lg mx-auto">
            We&apos;re always improving. If you know a provider we should benchmark or
            have feedback on our methodology, reach out to the team.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/contact"
              className="px-6 py-3 bg-geospatial hover:bg-geospatial-dark text-white font-medium rounded-lg transition-colors"
            >
              Contact Us
            </Link>
            <a
              href="mailto:host@serverpicks.net"
              className="px-6 py-3 border border-ever-600 hover:border-geospatial text-ever-400 hover:text-white font-medium rounded-lg transition-all"
            >
              host@serverpicks.net
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
