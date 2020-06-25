import React, { useRef, useState } from 'react';
import PropTypes from 'prop-types';
import { StaticQuery, graphql } from 'gatsby';
import Head from '../head/head';
import Header from '../header/header';
import Footer from '../footer/footer';
import '../../style.css';
import Breadcrumbs from '../breadcrumb/breadcrumb';
import GoogleAnalytics from '../google-analytics/google-analytics';
import Menu from '../../../lib/ssw.megamenu/menu/menu';
import MobileMenu from '../../../lib/ssw.megamenu/mobile-menu/mobile-menu';
import { config } from '@fortawesome/fontawesome-svg-core';
import '@fortawesome/fontawesome-svg-core/styles.css';

config.autoAddCss = false;
const Layout = ({
  children,
  displayActions,
  ruleUri,
  pageTitle,
  crumbs,
  crumbLabel,
}) => {
  const node = useRef();
  const [isMenuOpened, setIsMenuOpened] = useState(false);

  const actionOnToggleClick = () => {
    setIsMenuOpened(!isMenuOpened);
  };

  const handleClick = (e) => {
    if (node.current.contains(e.target)) {
      setIsMenuOpened(false);
    }
  };

  return (
    <div
      style={{
        overflow: isMenuOpened ? 'hidden' : 'auto',
      }}
    >
      {/* eslint-disable-next-line jsx-a11y/no-static-element-interactions */}
      <div
        ref={node}
        onMouseDown={isMenuOpened ? (event) => handleClick(event) : null}
        style={{
          transform: isMenuOpened ? 'translateX(84%)' : 'translateX(0px)',
        }}
      >
        <div className="flex flex-col min-h-screen main-container">
          <Head pageTitle={pageTitle} />
          <Header displayActions={displayActions} ruleUri={ruleUri} />
          <GoogleAnalytics pageTitle={pageTitle}></GoogleAnalytics>
          <Menu onClickToggle={() => actionOnToggleClick()}></Menu>
          {crumbs ? (
            <Breadcrumbs crumbs={crumbs} crumbLabel={crumbLabel} />
          ) : (
            <div></div>
          )}
          <main className="flex-1">{children}</main>
        </div>
        <Footer />
      </div>
      <MobileMenu isMenuOpened={isMenuOpened}></MobileMenu>
    </div>
  );
};

Layout.propTypes = {
  children: PropTypes.node.isRequired,
  data: PropTypes.object.isRequired,
  displayActions: PropTypes.bool.isRequired,
  ruleUri: PropTypes.string,
  pageTitle: PropTypes.string,
  crumbs: PropTypes.array,
  crumbLabel: PropTypes.string,
};

const LayoutWithQuery = (props) => (
  <StaticQuery
    query={graphql`
      query LayoutQuery {
        site {
          siteMetadata {
            siteTitle
          }
        }
      }
    `}
    render={(data) => <Layout data={data} {...props} />}
  />
);

LayoutWithQuery.propTypes = {
  children: PropTypes.node.isRequired,
};

export default LayoutWithQuery;
