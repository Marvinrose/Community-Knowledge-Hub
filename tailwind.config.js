/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ "./templates/**/*.html",
    "./articles/templates/**/*.html",],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}

