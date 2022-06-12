/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  typescript: {
    ignoreBuildErrors: true,
  },
  experimental: {
    outputStandalone: true,
  },
  trailingSlash: true,
  env: {
    PUBLIC_BACKEND_API_URL: process.env.PUBLIC_BACKEND_API_URL,
  },
}

module.exports = nextConfig
