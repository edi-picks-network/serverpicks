"use client";

import { useState } from "react";
import type { Metadata } from "next";
import { Mail, MapPin, Clock, Send } from "lucide-react";

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    subject: "",
    message: "",
  });
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // In production, this would send to an API endpoint
    setSubmitted(true);
    setTimeout(() => setSubmitted(false), 5000);
  };

  return (
    <div className="relative pt-32 pb-20 px-6">
      <div className="max-w-[1100px] mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <span className="inline-block text-xs font-semibold uppercase tracking-wider text-[#2563EB] bg-[#162540] px-3 py-1.5 rounded-md mb-4">
            Contact
          </span>
          <h1 className="text-3xl md:text-4xl font-extrabold text-[#F0F2FE] tracking-tight mb-3">
            Get in Touch
          </h1>
          <p className="text-lg text-[#839BBE] max-w-xl mx-auto">
            Have a question, suggestion, or want to list your hosting provider? We&apos;d love to
            hear from you.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 max-w-[1000px] mx-auto">
          {/* Contact Form */}
          <div className="lg:col-span-2">
            <div className="bg-[#0F1F2D] border border-[#1E3A5F] rounded-xl p-8">
              <h2 className="text-xl font-bold text-[#F0F2FE] mb-6">Send Us a Message</h2>

              {submitted ? (
                <div className="bg-[#162540] border border-[#60A5FA]/30 rounded-lg p-6 text-center">
                  <div className="w-12 h-12 rounded-full bg-[#60A5FA]/10 flex items-center justify-center mx-auto mb-3">
                    <Send className="w-6 h-6 text-[#60A5FA]" />
                  </div>
                  <p className="text-[#F0F2FE] font-semibold text-lg mb-1">Message Sent!</p>
                  <p className="text-[#839BBE] text-sm">
                    Thank you for reaching out. We&apos;ll get back to you within 24 hours.
                  </p>
                </div>
              ) : (
                <form onSubmit={handleSubmit} className="space-y-5">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                      <label className="block text-sm font-medium text-[#839BBE] mb-1.5">
                        Your Name
                      </label>
                      <input
                        type="text"
                        required
                        value={formData.name}
                        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                        className="w-full px-4 py-3 bg-[#0A0F1A] border border-[#1E3A5F] rounded-lg text-[#F0F2FE] placeholder:text-[#4A6080] focus:border-[#2563EB] focus:outline-none transition-colors"
                        placeholder="John Doe"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-[#839BBE] mb-1.5">
                        Email Address
                      </label>
                      <input
                        type="email"
                        required
                        value={formData.email}
                        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                        className="w-full px-4 py-3 bg-[#0A0F1A] border border-[#1E3A5F] rounded-lg text-[#F0F2FE] placeholder:text-[#4A6080] focus:border-[#2563EB] focus:outline-none transition-colors"
                        placeholder="john@company.com"
                      />
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-[#839BBE] mb-1.5">
                      Subject
                    </label>
                    <select
                      value={formData.subject}
                      onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
                      required
                      className="w-full px-4 py-3 bg-[#0A0F1A] border border-[#1E3A5F] rounded-lg text-[#F0F2FE] focus:border-[#2563EB] focus:outline-none transition-colors"
                    >
                      <option value="">Select a subject...</option>
                      <option value="general">General Inquiry</option>
                      <option value="provider-listing">List My Provider</option>
                      <option value="bug">Report a Bug</option>
                      <option value="suggestion">Feature Suggestion</option>
                      <option value="advertising">Advertising / Partnership</option>
                      <option value="other">Other</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-[#839BBE] mb-1.5">
                      Message
                    </label>
                    <textarea
                      required
                      rows={5}
                      value={formData.message}
                      onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                      className="w-full px-4 py-3 bg-[#0A0F1A] border border-[#1E3A5F] rounded-lg text-[#F0F2FE] placeholder:text-[#4A6080] focus:border-[#2563EB] focus:outline-none transition-colors resize-none"
                      placeholder="Tell us how we can help..."
                    />
                  </div>

                  <button
                    type="submit"
                    className="w-full sm:w-auto px-8 py-3 bg-[#2563EB] hover:bg-[#1D4ED8] text-white font-medium rounded-lg transition-colors flex items-center justify-center gap-2"
                  >
                    <Send className="w-4 h-4" />
                    Send Message
                  </button>
                </form>
              )}
            </div>
          </div>

          {/* Contact Info Sidebar */}
          <div className="space-y-5">
            <div className="bg-[#0F1F2D] border border-[#1E3A5F] rounded-xl p-6">
              <h3 className="text-sm font-semibold text-[#F0F2FE] mb-4 flex items-center gap-2">
                <Mail className="w-4 h-4 text-[#2563EB]" />
                Email Us
              </h3>
              <div className="space-y-2">
                <p className="text-sm text-[#839BBE]">
                  <strong className="text-[#F0F2FE]">Support:</strong>
                  <br />
                  <a href="mailto:support@serverpicks.net" className="text-[#2563EB] hover:underline">
                    support@serverpicks.net
                  </a>
                </p>
                <p className="text-sm text-[#839BBE]">
                  <strong className="text-[#F0F2FE]">General:</strong>
                  <br />
                  <a href="mailto:info@serverpicks.net" className="text-[#2563EB] hover:underline">
                    info@serverpicks.net
                  </a>
                </p>
                <p className="text-sm text-[#839BBE]">
                  <strong className="text-[#F0F2FE]">Press:</strong>
                  <br />
                  <a href="mailto:info@serverpicks.net" className="text-[#2563EB] hover:underline">
                    info@serverpicks.net
                  </a>
                </p>
              </div>
            </div>

            <div className="bg-[#0F1F2D] border border-[#1E3A5F] rounded-xl p-6">
              <h3 className="text-sm font-semibold text-[#F0F2FE] mb-4 flex items-center gap-2">
                <MapPin className="w-4 h-4 text-[#2563EB]" />
                Office
              </h3>
              <p className="text-sm text-[#839BBE] leading-relaxed">
                350 Fifth Avenue, Suite 3300
                <br />
                New York, NY 10118
                <br />
                United States
              </p>
            </div>

            <div className="bg-[#0F1F2D] border border-[#1E3A5F] rounded-xl p-6">
              <h3 className="text-sm font-semibold text-[#F0F2FE] mb-4 flex items-center gap-2">
                <Clock className="w-4 h-4 text-[#2563EB]" />
                Response Time
              </h3>
              <p className="text-sm text-[#839BBE]">
                We typically respond within <strong className="text-[#F0F2FE]">24 hours</strong> during
                business days.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
