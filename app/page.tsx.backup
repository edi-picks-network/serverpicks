"use client";

import { useState, useMemo } from "react";
import {
  Search, ArrowRight, Star, TrendingUp, BarChart3, BookOpen,
  CheckCircle2, HelpCircle, ChevronRight, Award, Users, Layers,
  Zap, Sparkles, Clock, ArrowUpRight, Mail, Send
} from "lucide-react";
import Link from "next/link";
import { ALL_TOOLS } from "@/data/tools";
import { BLOG_POSTS } from "@/data/blog-posts";

// 模板B：杂志对比式 — Email Marketing Tools Hub 适配版（红色系）

const ACCENT_COLOR = "#E63946";

export default function HomePage() {
  const [searchQuery, setSearchQuery] = useState("");

  const vsComparisons = useMemo(() => {
    const cats = [...new Set(ALL_TOOLS.map(t => t.category))].slice(0, 3);
    return cats.map(cat => {
      const tools = ALL_TOOLS.filter(t => t.category === cat).sort((a, b) => b.rating - a.rating).slice(0, 2);
      return { category: cat, toolA: tools[0], toolB: tools[1] };
    });
  }, [ALL_TOOLS]);

  const categoryCards = useMemo(() => {
    const m = new Map<string, { count: number; avgRating: number }>();
    for (const t of ALL_TOOLS) {
      if (!m.has(t.category)) m.set(t.category, { count: 0, avgRating: 0 });
      const s = m.get(t.category)!; s.count++; s.avgRating += t.rating;
    }
    return [...m.entries()].map(([name, d]) => ({ name, count: d.count, avgRating: Math.round((d.avgRating / d.count) * 10) / 10 })).sort((a, b) => b.count - a.count).slice(0, 8);
  }, [ALL_TOOLS]);

  const latestReviews = useMemo(() => [...BLOG_POSTS].sort((a: any, b: any) => new Date(b.date).getTime() - new Date(a.date).getTime()).slice(0, 4), [BLOG_POSTS]);

  const buyingGuides = useMemo(() => categoryCards.slice(0, 3).map(c => ({
    title: `How to Choose ${c.name} Software in 2026`,
    excerpt: `A practical guide to evaluating ${c.name.toLowerCase()} tools for your team size, budget, and use case.`,
    readTime: "8 min read",
    icon: c.name === "CRM" ? TrendingUp : c.name === "Marketing" ? Zap : Layers,
  })), [categoryCards]);

  const stats = useMemo(() => ({
    totalTools: ALL_TOOLS.length, totalCategories: new Set(ALL_TOOLS.map(t => t.category)).size,
    totalReviews: ALL_TOOLS.reduce((sum, t) => sum + (t.reviewCount || 0), 0),
    avgRating: (ALL_TOOLS.reduce((sum, t) => sum + t.rating, 0) / ALL_TOOLS.length).toFixed(1),
  }), [ALL_TOOLS]);

  const searchSuggestions = useMemo(() => {
    if (searchQuery.length < 2) return [];
    return ALL_TOOLS.filter(t => t.name.toLowerCase().includes(searchQuery.toLowerCase()) || t.category.toLowerCase().includes(searchQuery.toLowerCase())).slice(0, 5);
  }, [searchQuery, ALL_TOOLS]);

  return (
    <div className="min-h-screen bg-[#0A0A0F]">
      <section className="relative pt-32 pb-16 px-6 overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-b from-[#0A0A0F] via-[#1A0A0A] to-[#0A0A0F]" />
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-[400px] rounded-full opacity-[0.08] blur-[100px]" style={{ background: `radial-gradient(circle, ${ACCENT_COLOR}, transparent)` }} />
        <div className="relative max-w-6xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full text-sm bg-[#1A0F0F] border border-[#2A1A1A] mb-6">
            <Sparkles className="w-4 h-4" style={{ color: ACCENT_COLOR }} />
            <span className="text-gray-300">Expert reviews &amp; email marketing comparisons</span>
          </div>
          <h1 className="text-5xl md:text-6xl font-bold text-white leading-tight mb-6">
            Find the Perfect{" "}
            <span className="text-transparent bg-clip-text" style={{ backgroundImage: `linear-gradient(135deg, ${ACCENT_COLOR}, #F43F5E)` }}>Email Marketing Stack</span>
          </h1>
          <p className="text-lg text-gray-400 max-w-2xl mx-auto mb-10">In-depth comparisons, unbiased reviews, and buying guides — we help you make confident email marketing decisions backed by real data.</p>
          <div className="max-w-xl mx-auto relative">
            <div className="flex items-center bg-[#1A0F0F] border border-[#2A1A1A] rounded-xl px-5 py-3.5">
              <Search className="w-5 h-5 text-gray-500 mr-3" />
              <input type="text" placeholder={`Search ${stats.totalTools}+ tools across ${stats.totalCategories} categories...`} value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} className="bg-transparent text-white placeholder-gray-500 outline-none flex-1 text-base" />
            </div>
            {searchSuggestions.length > 0 && (
              <div className="absolute top-full mt-2 left-0 right-0 bg-[#1A0F0F] border border-[#2A1A1A] rounded-xl z-50 overflow-hidden">
                {searchSuggestions.map(tool => (
                  <Link key={tool.id} href={`/tools/${tool.id}`} className="flex items-center gap-3 px-5 py-3 hover:bg-[#2A1515] transition-colors text-left">
                    <div className="w-8 h-8 rounded-lg bg-[#2A1515] flex items-center justify-center"><Layers className="w-4 h-4" style={{ color: ACCENT_COLOR }} /></div>
                    <div className="flex-1"><p className="text-white text-sm font-medium">{tool.name}</p><p className="text-gray-500 text-xs">{tool.category}</p></div>
                    <div className="flex items-center gap-1"><Star className="w-3.5 h-3.5 text-yellow-500 fill-yellow-500" /><span className="text-gray-300 text-sm">{tool.rating}</span></div>
                  </Link>
                ))}
              </div>
            )}
          </div>
        </div>
      </section>

      <section className="px-6 py-8">
        <div className="max-w-6xl mx-auto">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {[
              { icon: BarChart3, label: "Tools Reviewed", value: stats.totalTools },
              { icon: Layers, label: "Categories", value: stats.totalCategories },
              { icon: Users, label: "User Reviews", value: stats.totalReviews > 10000 ? `${(stats.totalReviews / 1000).toFixed(0)}K+` : stats.totalReviews },
              { icon: Award, label: "Avg Rating", value: `★ ${stats.avgRating}` },
            ].map((item, i) => (
              <div key={i} className="bg-[#0F0A0A] border border-[#1F1515] rounded-xl p-5 text-center">
                <item.icon className="w-5 h-5 mx-auto mb-2" style={{ color: ACCENT_COLOR }} />
                <p className="text-2xl font-bold text-white">{item.value}</p>
                <p className="text-xs text-gray-500 mt-1">{item.label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="px-6 py-12">
        <div className="max-w-6xl mx-auto">
          <div className="flex items-center justify-between mb-8">
            <div><h2 className="text-2xl font-bold text-white">Head-to-Head Comparisons</h2><p className="text-gray-500 text-sm mt-1">We pit the top tools against each other</p></div>
            <Link href="/comparisons" className="text-sm flex items-center gap-1 hover:underline" style={{ color: ACCENT_COLOR }}>View all <ArrowRight className="w-3.5 h-3.5" /></Link>
          </div>
          <div className="grid md:grid-cols-3 gap-6">
            {vsComparisons.map((pair, i) => pair.toolA && pair.toolB ? (
              <div key={i} className="bg-[#0F0A0A] border border-[#1F1515] rounded-xl p-5 hover:border-[#3A2020] transition-all">
                <p className="text-xs text-gray-500 uppercase tracking-wider mb-4">{pair.category}</p>
                <div className="flex items-center gap-3 mb-3">
                  <div className="w-10 h-10 rounded-lg bg-[#1A0F0F] flex items-center justify-center text-lg font-bold text-[#E63946]">{pair.toolA.name.charAt(0)}</div>
                  <div className="flex-1"><p className="text-white font-semibold text-sm">{pair.toolA.name}</p><div className="flex items-center gap-1"><Star className="w-3 h-3 text-yellow-500 fill-yellow-500" /><span className="text-gray-300 text-xs">{pair.toolA.rating}</span></div></div>
                  <Link href={`/tools/${pair.toolA.id}`} className="text-xs px-3 py-1.5 rounded-lg border transition-colors" style={{ borderColor: ACCENT_COLOR, color: ACCENT_COLOR }}>Review</Link>
                </div>
                <div className="flex items-center gap-3 mb-3"><div className="flex-1 h-px bg-[#2A1A1A]" /><span className="text-xs font-bold text-gray-500">VS</span><div className="flex-1 h-px bg-[#2A1A1A]" /></div>
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg bg-[#1A0F0F] flex items-center justify-center text-lg font-bold text-[#E63946]">{pair.toolB.name.charAt(0)}</div>
                  <div className="flex-1"><p className="text-white font-semibold text-sm">{pair.toolB.name}</p><div className="flex items-center gap-1"><Star className="w-3 h-3 text-yellow-500 fill-yellow-500" /><span className="text-gray-300 text-xs">{pair.toolB.rating}</span></div></div>
                  <Link href={`/tools/${pair.toolB.id}`} className="text-xs px-3 py-1.5 rounded-lg border transition-colors" style={{ borderColor: ACCENT_COLOR, color: ACCENT_COLOR }}>Review</Link>
                </div>
                <Link href={`/comparison/${pair.toolA.id}-vs-${pair.toolB.id}`} className="mt-4 w-full text-xs py-2 rounded-lg flex items-center justify-center gap-1 transition-colors" style={{ backgroundColor: `${ACCENT_COLOR}15`, color: ACCENT_COLOR }}>Which is right for you? <HelpCircle className="w-3 h-3" /></Link>
              </div>
            ) : null)}
          </div>
        </div>
      </section>

      <section className="px-6 py-12">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-2xl font-bold text-white mb-2">Browse by Category</h2>
          <p className="text-gray-500 text-sm mb-8">Explore tools organized by your marketing needs</p>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {categoryCards.map(cat => (
              <Link key={cat.name} href={`/category/${cat.name.toLowerCase().replace(/ & /g, "-").replace(/ /g, "-")}`} className="group bg-[#0F0A0A] border border-[#1F1515] rounded-xl p-5 hover:border-[#3A2020] transition-all">
                <div className="flex items-center justify-between mb-3">
                  <div className="w-9 h-9 rounded-lg flex items-center justify-center" style={{ backgroundColor: `${ACCENT_COLOR}15` }}><Layers className="w-4 h-4" style={{ color: ACCENT_COLOR }} /></div>
                  <span className="text-xs px-2 py-0.5 rounded-full bg-[#1A0F0F] text-gray-400">{cat.count} tools</span>
                </div>
                <h3 className="text-white font-semibold text-sm mb-1">{cat.name}</h3>
                <p className="text-gray-500 text-xs leading-relaxed">Explore top {cat.name.toLowerCase()} tools</p>
                <div className="flex items-center gap-1 mt-2"><Star className="w-3 h-3 text-yellow-500 fill-yellow-500" /><span className="text-gray-400 text-xs">{cat.avgRating} avg rating</span></div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      <section className="px-6 py-12">
        <div className="max-w-6xl mx-auto">
          <div className="flex items-center justify-between mb-8">
            <div><h2 className="text-2xl font-bold text-white">Latest Reviews &amp; Analysis</h2><p className="text-gray-500 text-sm mt-1">In-depth, unbiased, and up-to-date</p></div>
            <Link href="/blog" className="text-sm flex items-center gap-1 hover:underline" style={{ color: ACCENT_COLOR }}>View all <ArrowRight className="w-3.5 h-3.5" /></Link>
          </div>
          <div className="grid md:grid-cols-2 gap-6">
            {latestReviews[0] && (
              <Link href={`/blog/${latestReviews[0].slug}`} className="md:col-span-1 bg-[#0F0A0A] border border-[#1F1515] rounded-xl p-6 hover:border-[#3A2020] transition-all group">
                <div className="flex items-center gap-2 mb-4">
                  <span className="text-xs px-2.5 py-1 rounded-full" style={{ backgroundColor: `${ACCENT_COLOR}15`, color: ACCENT_COLOR }}>{latestReviews[0].category || "Featured"}</span>
                  <span className="text-xs text-gray-500 flex items-center gap-1"><Clock className="w-3 h-3" />{latestReviews[0].readTime || "5 min"}</span>
                </div>
                <h3 className="text-lg font-bold text-white mb-3 group-hover:underline">{latestReviews[0].title}</h3>
                <p className="text-gray-400 text-sm leading-relaxed mb-4 line-clamp-3">{latestReviews[0].excerpt}</p>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2"><div className="w-7 h-7 rounded-full bg-[#1A0F0F] flex items-center justify-center text-xs text-gray-300">{latestReviews[0].author?.charAt(0) || "E"}</div><span className="text-xs text-gray-500">{latestReviews[0].author || "Editor"} · {latestReviews[0].date}</span></div>
                  <span className="text-xs flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity" style={{ color: ACCENT_COLOR }}>Read more <ArrowUpRight className="w-3 h-3" /></span>
                </div>
              </Link>
            )}
            <div className="flex flex-col gap-4">
              {latestReviews.slice(1, 4).map((post, i) => (
                <Link key={post.slug || i} href={`/blog/${post.slug}`} className="flex gap-4 bg-[#0F0A0A] border border-[#1F1515] rounded-xl p-4 hover:border-[#3A2020] transition-all group">
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2 mb-1"><span className="text-[10px] px-2 py-0.5 rounded-full bg-[#1A0F0F] text-gray-400">{post.category || "Article"}</span><span className="text-[10px] text-gray-600">{post.readTime || "5 min"}</span></div>
                    <h4 className="text-sm font-semibold text-white group-hover:underline line-clamp-2">{post.title}</h4><p className="text-xs text-gray-500 mt-1">{post.date}</p>
                  </div>
                  <ArrowRight className="w-4 h-4 text-gray-600 self-center flex-shrink-0" />
                </Link>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="px-6 py-12">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-2xl font-bold text-white mb-2">Buying Guides</h2>
          <p className="text-gray-500 text-sm mb-8">Step-by-step guides to choosing the right software</p>
          <div className="grid md:grid-cols-3 gap-6">
            {buyingGuides.map((guide, i) => (
              <div key={i} className="bg-[#0F0A0A] border border-[#1F1515] rounded-xl p-6 hover:border-[#3A2020] transition-all group cursor-pointer">
                <guide.icon className="w-8 h-8 mb-4" style={{ color: ACCENT_COLOR }} />
                <h3 className="text-white font-semibold mb-2 group-hover:underline">{guide.title}</h3>
                <p className="text-gray-400 text-sm leading-relaxed mb-4">{guide.excerpt}</p>
                <div className="flex items-center justify-between"><span className="text-xs text-gray-500">{guide.readTime}</span><span className="text-xs flex items-center gap-1" style={{ color: ACCENT_COLOR }}>Read guide <ChevronRight className="w-3 h-3" /></span></div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="px-6 py-16">
        <div className="max-w-6xl mx-auto text-center">
          <div className="bg-gradient-to-r from-[#0F0A0A] to-[#1A0F0F] border border-[#2A1A1A] rounded-2xl p-10 md:p-14">
            <CheckCircle2 className="w-10 h-10 mx-auto mb-4" style={{ color: ACCENT_COLOR }} />
            <h2 className="text-2xl md:text-3xl font-bold text-white mb-3">Ready to build your email marketing stack?</h2>
            <p className="text-gray-400 max-w-xl mx-auto mb-8">Browse our curated collection of {stats.totalTools}+ tools across {stats.totalCategories} categories.</p>
            <Link href="/all-tools" className="inline-flex items-center gap-2 px-8 py-3.5 rounded-xl text-white font-semibold transition-all hover:scale-105" style={{ backgroundColor: ACCENT_COLOR }}>Browse All Tools <ArrowRight className="w-4 h-4" /></Link>
          </div>
        </div>
      </section>
    </div>
  );
}
