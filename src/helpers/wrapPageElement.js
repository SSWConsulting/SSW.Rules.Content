import React from 'react';
//import Transition from '../components/transition/transition.js';
import PropTypes from 'prop-types';
import Layout from '../components/layout/layout';

const wrapPageElement = ({ element, props }) => {
  const markdown =
    props && props.data && props.data.markdownRemark
      ? props.data.markdownRemark
      : null;
  const crumbs =
    props &&
    props.pageContext &&
    props.pageContext.breadcrumb &&
    props.pageContext.breadcrumb.crumbs
      ? props.pageContext.breadcrumb.crumbs
      : null;
  return (
    //<Transition {...props}>
    <Layout
      {...props}
      crumbs={crumbs}
      crumbLabel={markdown ? markdown.frontmatter.title : null}
      displayActions={markdown ? true : false}
      ruleUri={markdown ? markdown.parent.relativePath : null}
    >
      {element}
    </Layout>
    // </Transition>
  );
};

wrapPageElement.propTypes = {
  element: PropTypes.any,
  props: PropTypes.any,
  data: PropTypes.any,
  pageContext: PropTypes.any,
};

export default wrapPageElement;
