import React from 'react';
import { graphql } from "gatsby";
import Layout from '../components/layout/layout';
export default function Category({ data, 
    pageContext: {
      breadcrumb: { crumbs },
    } 
  }) {
  const post = data.markdownRemark
  return (
    <Layout crumbs={crumbs} displayActions={false}>
      <div>
        <h1>{post.frontmatter.title}</h1>
        <div dangerouslySetInnerHTML={{ __html: post.html }} />
      </div>
    </Layout>
  )
}
export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
      }
    }
  }
`