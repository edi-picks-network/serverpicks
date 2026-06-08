"use client";

import { useState, useMemo } from "react";
import { ALL_TOOLS } from "@/data/tools";
import { BLOG_POSTS } from "@/data/blog-posts";
import Link from "next/link";

export default function HomePage() {
  const [searchQuery, setSearchQuery] = useState("");

  const categories = useMemo(() => {
    const map = new Map<string, { count: number }>();
    for (const tool of ALL_TOOLS) {
      const cat = tool.category || "Other";
      if (!map.has(cat)) map.set(cat, { count: 0 });
      map.get(cat)!.count++;
    }
    return Array.from(map.entries())
      .map(([name, data]) => ({ name, count: data.count }))
      .sort((a, b) => b.count - a.count);
  }, []);

  const filteredTools = useMemo(() => {
    if (!searchQuery.trim()) return ALL_TOOLS;
    const q = searchQuery.toLowerCase();
    return ALL_TOOLS.filter(
      (t) =>
        t.name.toLowerCase().includes(q) ||
        t.description.toLowerCase().includes(q) ||
        (t.category && t.category.toLowerCase().includes(q))
    );
  }, [searchQuery]);

  const latestPosts = useMemo(
    () =>
      [...BLOG_POSTS]
        .sort((a: any, b: any) => new Date(b.date).getTime() - new Date(a.date).getTime())
        .slice(0, 3),
    []
  );

  return (
    <div>
      {/* HERO — Deep blue gradient */}
      <section className="relative bg-gradient-to-br from-blue-900 via-blue-800 to-indigo-900 text-white overflow-hidden">
        <div className="max-w-6xl mx-auto px-6 pt-24 pb-16 md:pt-32 md:pb-24">
          <div className="max-w-3xl">
            <span className="inline-block text-sm font-semibold text-blue-200 bg-blue-800/50 px-4 py-1.5 rounded-full mb-6">
              Trusted by 10,000+ developers
            </span>
            <h1 className="text-5xl md:text-7xl font-black tracking-tight leading-[1.05] mb-6">
              Find Your{" "}
              <span className="text-blue-300">Perfect Host</span>
            </h1>
            <p className="text-xl text-blue-200 max-w-2xl mb-10 leading-relaxed">
              Side-by-side comparisons of cloud providers, VPS hosts, and
              dedicated server companies. No sponsored rankings — just honest
              benchmarks.
            </p>
            <div className="w-full max-w-lg">
              <div className="flex items-center bg-white rounded-xl shadow-sm overflow-hidden">
                <svg className="ml-5 w-5 h-5 text-gray-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-4.35-4.35M11 19a8 8 0 100-16 8 8 0 000 16z" />
                </svg>
                <input
                  type="search"
                  placeholder="Search providers by name or category…"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="flex-1 py-4 px-3 bg-transparent text-gray-900 placeholder-gray-400 outline-none text-base"
                />
                <Link
                  href={filteredTools.length > 0 ? `/tools/${filteredTools[0].id}` : "/"}
                  className="mr-2 px-5 py-2.5 bg-blue-700 hover:bg-blue-800 text-white text-sm font-semibold rounded-lg transition-colors"
                >
                  Search
                </Link>
              </div>
            </div>
          </div>
        </div>
        <div className="absolute -top-20 -right-20 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl" />
      </section>

      {/* Stats bar */}
      <section className="bg-white border-b border-gray-100">
        <div className="max-w-6xl mx-auto px-6 py-6 grid grid-cols-3 gap-8">
          <div className="text-center">
            <p className="text-3xl font-black text-blue-700">{ALL_TOOLS.length}</p>
            <p className="text-sm text-gray-500">Providers Reviewed</p>
          </div>
          <div className="text-center">
            <p className="text-3xl font-black text-blue-700">{categories.length}</p>
            <p className="text-sm text-gray-500">Categories</p>
          </div>
          <div className="text-center">
            <p className="text-3xl font-black text-blue-700">{BLOG_POSTS.length}</p>
            <p className="text-sm text-gray-500">Articles</p>
          </div>
        </div>
      </section>

      {/* Categories */}
      <section className="py-12">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-2">Categories</h2>
          <p className="text-gray-500 mb-8">Browse by provider type</p>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {categories.slice(0, 8).map((cat) => (
              <Link
                key={cat.name}
                href={`/category/${cat.name.toLowerCase().replace(/\s+/g, "-")}`}
                className="group bg-white border border-gray-200 rounded-xl p-5 hover:border-blue-300 hover:shadow-md transition-all"
              >
                <h3 className="font-semibold text-gray-900 group-hover:text-blue-700 transition-colors">{cat.name}</h3>
                <p className="text-sm text-gray-400 mt-1">{cat.count} providers</p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* All Providers */}
      <section className="py-12 bg-gray-50">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-8">
            {searchQuery ? `Results for "${searchQuery}"` : "All Providers"}
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {filteredTools.slice(0, 30).map((tool) => (
              <Link
                key={tool.id}
                href={`/tools/${tool.id}`}
                className="group bg-white border border-gray-200 rounded-xl p-5 hover:border-blue-300 hover:shadow-lg hover:-translate-y-0.5 transition-all"
              >
                <div className="flex items-center gap-3 mb-3">
                  <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-100 to-indigo-100 flex items-center justify-center text-blue-700 font-bold text-sm">
                    {tool.name.charAt(0)}
                  </div>
                  <div className="min-w-0 flex-1">
                    <h3 className="font-semibold text-gray-900 group-hover:text-blue-700 transition-colors truncate">{tool.name}</h3>
                    <span className="text-xs text-gray-400 uppercase tracking-wide">{tool.category}</span>
                  </div>
                  <div className="flex items-center gap-1 bg-blue-50 px-2 py-1 rounded-md">
                    <span className="text-yellow-500 text-xs">★</span>
                    <span className="text-xs font-bold text-gray-700">{tool.rating}</span>
                  </div>
                </div>
                <p className="text-sm text-gray-500 leading-relaxed line-clamp-2 mb-3">{tool.description}</p>
                <div className="pt-3 border-t border-gray-100 text-xs font-medium text-blue-700 group-hover:text-blue-800">
                  View Details →
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Top Rated */}
      <section className="py-12">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-2">★ Top Rated</h2>
          <p className="text-gray-500 mb-8">Highest-rated providers by user reviews</p>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {ALL_TOOLS.filter((t) => t.rating >= 4.7).slice(0, 3).map((tool) => (
              <Link
                key={tool.id}
                href={`/tools/${tool.id}`}
                className="group bg-white border-2 border-blue-100 rounded-xl p-6 hover:border-blue-300 hover:shadow-lg transition-all"
              >
                <div className="flex items-center gap-1 text-amber-400 mb-2">
                  {Array.from({ length: 5 }).map((_, i) => <span key={i}>★</span>)}
                </div>
                <h3 className="text-lg font-bold text-gray-900 mb-1">{tool.name}</h3>
                <p className="text-sm text-gray-500 line-clamp-2">{tool.description}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Blog */}
      {latestPosts.length > 0 && (
        <section className="py-12 bg-gray-50">
          <div className="max-w-6xl mx-auto px-6">
            <div className="flex items-center justify-between mb-8">
              <h2 className="text-2xl font-bold text-gray-900">Latest Articles</h2>
              <Link href="/blog" className="text-sm font-medium text-blue-700 hover:text-blue-800">View all →</Link>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {latestPosts.map((post: any) => (
                <Link key={post.slug} href={`/blog/${post.slug}`} className="group">
                  <article className="bg-white border border-gray-200 rounded-xl p-6 hover:border-blue-200 hover:shadow-md transition-all h-full flex flex-col">
                    <span className="text-xs font-semibold text-blue-700 uppercase tracking-wider mb-2">{post.category || "Article"}</span>
                    <h3 className="font-bold text-gray-900 mb-2 group-hover:text-blue-700 transition-colors leading-snug">{post.title}</h3>
                    <p className="text-sm text-gray-500 flex-grow line-clamp-3">{post.excerpt}</p>
                    <div className="mt-4 pt-3 border-t border-gray-100 text-xs text-gray-400">{post.date} · {post.readTime} min read</div>
                  </article>
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* CTA */}
      <section className="py-16 bg-gradient-to-r from-blue-800 to-indigo-900 text-white">
        <div className="max-w-3xl mx-auto px-6 text-center">
          <h2 className="text-3xl font-bold mb-4">Compare Before You Commit</h2>
          <p className="text-blue-200 mb-8">See how {ALL_TOOLS.length} hosting providers stack up — real benchmarks, real reviews.</p>
          <Link
            href="/all-tools"
            className="inline-flex items-center gap-2 px-8 py-3.5 bg-white text-blue-800 font-bold rounded-xl hover:bg-blue-50 transition-colors shadow-lg"
          >
            Browse All Providers →
          </Link>
        </div>
      </section>
    </div>
  );
}
