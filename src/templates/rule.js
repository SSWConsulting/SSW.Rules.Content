import React from 'react';
import { graphql } from 'gatsby';
import Layout from '../components/layout/layout';
import PropTypes from 'prop-types';
export default function Rule({
  data,
  pageContext: {
    breadcrumb: { crumbs },
  },
}) {
  const rule = data.markdownRemark;
  return (
    <Layout
      crumbs={crumbs}
      crumbLabel={rule.frontmatter.title}
      displayActions={false}
    >
      <div>
        <h1>{rule.frontmatter.title}</h1>
        <div dangerouslySetInnerHTML={{ __html: rule.html }} />
      </div>
    </Layout>
  );
}

Rule.propTypes = {
  data: PropTypes.object.isRequired,
  pageContext: PropTypes.object.isRequired,
};

export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
      }
    }
  }
`;
