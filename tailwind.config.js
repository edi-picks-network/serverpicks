/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        deep: {
          DEFAULT: '#1A0A0A',
          100: '#2D0F0F',
          200: '#401616',
          300: '#5F1E1E',
          400: '#802828',
          500: '#E63946',
        },
        muted: {
          DEFAULT: '#80504A',
          light: '#BE8A83',
        },
        surface: '#FEF2F0',
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
