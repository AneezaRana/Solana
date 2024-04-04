/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    screens: {
      'xs': '200px',
      'sm': '640px',
      'md': '768px', 
      'lg': '1024px',
    },
    extend: {
      display: {
        'contents': 'contents',
      },
      colors: {
        primary:'#848895',
        secondary: '#00ff00',
        'customGray': '#848895',
        'customBlue': '#618ADC'
      },
      backgroundColor: {
        navColor: '#00000099'
      },
      backgroundImage: {
        'custom-bg': "url('assets/custom-bg.jpeg')",
      },
    },
  },
  plugins: [],
}

