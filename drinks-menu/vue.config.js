const webpack = require ("webpack");
const { defineConfig } = require('@vue/cli-service');
module.exports = defineConfig({
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    allowedHosts: 'all',
    client: {
      webSocketURL: 'wss://dev.drinks.mcgeld.com/ws'
    },
    headers: {
      'Access-Control-Allow-Origin': '*', // Allows CORS for WebSocket
    },
    hot: true,
    watchFiles: ['src/**/*'],
  },
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        __VUE_OPTIONS_API__: JSON.stringify(true),
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: JSON.stringify(true),
      }),
    ],
  },
});
