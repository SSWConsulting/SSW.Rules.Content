import React from 'react';
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

export default Index;
