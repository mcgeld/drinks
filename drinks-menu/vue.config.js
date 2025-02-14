const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  outputDir: process.env.VUE_BUILD_ENV === 'development'
    ? '/var/www/websites/drinks/dev-dist'
    : '/var/www/websites/drinks/drinks-menu/dist',

	devServer: {
		host: '0.0.0.0',
		port: 8080,
		allowedHosts: "all"
	}
})
