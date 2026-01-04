/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
      extend: {
        // Adding a custom "Socratic" color palette for a professional look
        colors: {
          socrates: {
            light: '#f8fafc',
            gold: '#d4af37',
            ancient: '#2c3e50',
          }
        }
      },
    },
    plugins: [],
  }