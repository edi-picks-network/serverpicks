"use client";
import { motion } from 'framer-motion';
import { Star, ArrowRight, BarChart3, ShieldCheck, MessageSquare, Users, CreditCard, Briefcase } from 'lucide-react';
import type { LucideIcon } from 'lucide-react';

interface Tool {
  id: string;
  name: string;
  category: string;
  rating: number;
  reviews: number;
  description: string;
  icon: LucideIcon;
  pricing: string;
}

const FEATURED_TOOLS: Tool[] = [
  {
    id: 'tool-1',
    name: 'DataMetrics Pro',
    category: 'Analytics',
    rating: 4.9,
    reviews: 128,
    description: 'Advanced enterprise analytics platform with real-time predictive modeling.',
    icon: BarChart3,
    pricing: 'From $99/mo',
  },
  {
    id: 'tool-2',
    name: 'SecureGuard CRM',
    category: 'CRM & Sales',
    rating: 4.8,
    reviews: 342,
    description: 'End-to-end encrypted customer relationship management for finance teams.',
    icon: ShieldCheck,
    pricing: 'Contact Sales',
  },
  {
    id: 'tool-3',
    name: 'TeamSync Hub',
    category: 'Collaboration',
    rating: 4.7,
    reviews: 89,
    description: 'Unified communication and project management suite for remote teams.',
    icon: MessageSquare,
    pricing: 'Freemium',
  },
  {
    id: 'tool-4',
    name: 'HR TalentFlow',
    category: 'Human Resources',
    rating: 4.6,
    reviews: 215,
    description: 'Automated recruitment, onboarding, and payroll management system.',
    icon: Users,
    pricing: 'From $49/mo',
  },
  {
    id: 'tool-5',
    name: 'PayStream API',
    category: 'Finance',
    rating: 4.9,
    reviews: 512,
    description: 'Global B2B payment gateway API with built-in fraud prevention.',
    icon: CreditCard,
    pricing: 'Pay-as-you-go',
  },
  {
    id: 'tool-6',
    name: 'BizOps Flow',
    category: 'Operations',
    rating: 4.5,
    reviews: 76,
    description: 'No-code workflow automation specifically designed for operational efficiency.',
    icon: Briefcase,
    pricing: 'From $199/mo',
  },
];

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
    },
  },
};

const cardVariants = {
  hidden: { opacity: 0, y: 30 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: [0.4, 0, 0.2, 1] as [number, number, number, number] },
  },
};

export default function FeaturedTools() {
  return (
    <section id="featured" className="relative py-20 px-6">
      <div className="max-w-[1200px] mx-auto">
        {/* Section Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-100px' }}
          transition={{ duration: 0.5 }}
          className="flex items-center justify-between mb-10"
        >
          <div>
            <h2 className="text-2xl md:text-[2rem] font-bold text-[#F0F2FE] tracking-tight">
              Featured Hosting Providers
            </h2>
            <p className="text-[#839BBE] mt-1 text-base">
              Hand-picked hosting providers highly rated by users worldwide.
            </p>
          </div>
          <a
            href="#categories"
            className="hidden sm:flex items-center gap-1 text-[#2563EB] hover:text-[#60A5FA] font-medium text-sm transition-colors"
          >
            View All Categories
            <ArrowRight className="w-4 h-4" />
          </a>
        </motion.div>

        {/* Tool Cards Grid */}
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '-50px' }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
        >
          {FEATURED_TOOLS.map((tool) => {
            const Icon = tool.icon;
            return (
              <motion.article
                key={tool.id}
                variants={cardVariants}
                className="group bg-[#0F1F2D] border border-[#1E3A5F] rounded-xl p-6 card-hover cursor-pointer"
              >
                {/* Top Row: Icon + Rating */}
                <div className="flex items-start justify-between mb-4">
                  <div className="w-12 h-12 rounded-lg bg-[#162540] flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform duration-300">
                    <Icon className="w-6 h-6 text-[#2563EB]" />
                  </div>
                  <div className="flex items-center gap-1 bg-[#162540] px-2 py-1 rounded-md border border-[#1E3A5F]">
                    <Star className="w-4 h-4 text-[#F59E0B] fill-[#F59E0B]" />
                    <span className="text-sm font-semibold text-[#F0F2FE]">{tool.rating}</span>
                    <span className="text-sm text-[#4A6080]">({tool.reviews})</span>
                  </div>
                </div>

                {/* Name */}
                <h3 className="text-lg font-bold text-[#F0F2FE] mb-1 group-hover:text-[#2563EB] transition-colors">
                  {tool.name}
                </h3>

                {/* Category Badge */}
                <span className="inline-block text-xs font-semibold uppercase tracking-wider text-[#2563EB] bg-[#162540] px-2.5 py-1 rounded-md mb-3">
                  {tool.category}
                </span>

                {/* Description */}
                <p className="text-sm text-[#839BBE] mb-6 leading-relaxed">
                  {tool.description}
                </p>

                {/* Bottom Row: Pricing + CTA */}
                <div className="flex items-center justify-between pt-4 border-t border-[#1E3A5F]">
                  <span className="text-sm font-semibold text-[#F0F2FE]">{tool.pricing}</span>
                  <button className="px-4 py-1.5 text-xs font-medium text-[#839BBE] bg-transparent border border-[#1E3A5F] rounded-lg group-hover:bg-[#162540] group-hover:text-[#2563EB] group-hover:border-[#284880] transition-all">
                    Learn More
                  </button>
                </div>
              </motion.article>
            );
          })}
        </motion.div>

        {/* Mobile View All Button */}
        <div className="mt-8 sm:hidden flex justify-center">
          <button className="w-full px-6 py-3 text-sm font-medium text-[#839BBE] bg-[#0F1F2D] border border-[#1E3A5F] rounded-lg hover:bg-[#162540] transition-colors">
            View All Categories
          </button>
        </div>
      </div>
    </section>
  );
}
