import React from 'react';
import PropTypes from 'prop-types';
import ReactGA from 'react-ga';

ReactGA.initialize(process.env.GOOGLE_ANALYTICS);

const GoogleAnalytics = ({ pageTitle }) => (
  <>
    {typeof window !== 'undefined' &&
      ReactGA.pageview(window.location.pathname, null, pageTitle)}
  </>
);

GoogleAnalytics.propTypes = {
  pageTitle: PropTypes.string,
};

export default GoogleAnalytics;
