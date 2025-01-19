module.exports = {
  content: [
    "./src/**/*.{html,js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#ECF3FB',
          DEFAULT: '#0A192F',
          dark: '#0A192F',
        },
        secondary: {
          light: '#236, 243, 251',
          DEFAULT: '#10, 25, 47',
          dark: '#10, 25, 47',
        }
      },
      fontFamily: {
        'avenir': ['Avenir', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}