import React from 'react';
import { StaticQuery, graphql } from 'gatsby';
import Layout from '../components/layout/layout';
import PropTypes from 'prop-types';

const Index = ({
  pageContext: {
    breadcrumb: { crumbs },
  },
}) => (
  <Layout crumbs={crumbs} displayActions={false}>
    <div>
      <h1>SSW.Rules</h1>
      <h4>Ready to start!</h4>
    </div>
  </Layout>
);

Index.propTypes = {
  data: PropTypes.object.isRequired,
  search: PropTypes.object.isRequired,
  pageContext: PropTypes.object.isRequired,
  location: PropTypes.object.isRequired,
};

const IndexWithQuery = (props) => (
  <StaticQuery
    query={graphql`
      query HomepageQuery {
        rules: allMarkdownRemark(
          filter: { frontmatter: { type: { eq: "top_category" } } }
        ) {
          nodes {
            html
            frontmatter {
              type
              title
            }
            parent {
              ... on File {
                name
              }
            }
          }
        }
      }
    `}
    render={(data) => <Index {...data.HomepageQuery} {...props} />}
  />
);

export default IndexWithQuery;
