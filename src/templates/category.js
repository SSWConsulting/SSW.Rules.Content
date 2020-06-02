import React, { useRef } from 'react';
import { graphql, Link } from 'gatsby';
import Layout from '../components/layout/layout';
export default function Category({
  data,
  pageContext: {
    breadcrumb: { crumbs },
  },
}) {
  const linkRef = useRef();
  const category = data.markdownRemark;
  return (
    <Layout
      crumbs={crumbs}
      crumbLabel={category.frontmatter.title}
      displayActions={false}
    >
      <div>
        <h1>{category.frontmatter.title}</h1>
        <div dangerouslySetInnerHTML={{ __html: category.html }} />
        <br />
      </div>
      <ol className="list-decimal list-outside">
        {category.frontmatter.index.map((ruleUri, i) => {
          const rule = data.rule.nodes.find(
            (r) => r.frontmatter.uri === ruleUri
          );
          if (rule) {
            return (
              <>
                <li key={i} className="rule-title">
                  <Link ref={linkRef} to={`/${rule.frontmatter.uri}`}>
                    {rule.frontmatter.title}
                  </Link>
                </li>
                <div dangerouslySetInnerHTML={{ __html: rule.html }} />
                <br />
              </>
            );
          }
        })}
      </ol>
    </Layout>
  );
}
export const query = graphql`
  query($slug: String!, $index: [String]!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        title
        index
      }
    }
    rule: allMarkdownRemark(filter: { frontmatter: { uri: { in: $index } } }) {
      nodes {
        frontmatter {
          uri
          title
        }
        html
      }
    }
  }
`;
