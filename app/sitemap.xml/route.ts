import { MetadataRoute } from "next";

const BLOG_SLUGS = [
  "digitalocean-vs-linode-vs-vultr-2026",
    "aws-vs-azure-vs-google-cloud-2026",
    "aws-vs-azure-vs-gcp-vs-digitalocean-2026",
    "european-vps-showdown-2026-hetzner-ovhcloud-contabo-scaleway",
    "european-budget-vps-contabo-scaleway-ionos-2026",
    "managed-vs-unmanaged-vps-2026",
    "dedicated-server-vs-vps-vs-cloud-2026",
    "aws-vs-azure-vs-gcp-2026",
    "vps-security-hardening-2026",
    "from-shared-hosting-to-vps-migration-guide",
    "vps-vpn-guide-2026-deep-dive",
    "cloud-server-pricing-2026-cost-optimization",
    "vps-backup-disaster-recovery-2026",
] as const;

const TOOL_SLUGS = [
  "aws",
    "azure",
    "gcp",
    "digitalocean",
    "linode",
    "vultr",
    "alibaba-cloud",
    "oracle-cloud",
    "ibm-cloud",
    "tencent-cloud",
    "hetzner",
    "ovhcloud",
    "contabo",
    "scaleway",
    "ionos",
    "upcloud",
    "civo",
    "kamatera",
    "greencloudvps",
    "interserver",
    "cloudflare",
    "akamai",
    "fastly",
    "keycdn",
    "bunnynet",
    "stackpath",
    "amazoncloudfront",
    "googlecloudcdn",
    "azurecdn",
    "godaddy",
    "namecheap",
    "porkbun",
    "cloudflare-registrar",
    "amazon-route-53",
    "google-cloud-dns",
    "azure-dns",
    "let's-encrypt",
    "sectigo",
    "ssl.com",
    "cpanel",
    "plesk",
    "webmin",
    "cockpit",
    "ansible",
    "puppet",
    "chef",
    "terraform",
    "pulumi",
    "salt-project",
    "grafana",
    "prometheus",
    "datadog",
    "new-relic",
    "mongodb-atlas",
    "amazon-rds",
    "planetscale",
    "supabase",
    "neon",
    "railway",
] as const;

const CATEGORY_SLUGS = [
  "cdn-and-dns",
    "cloud-platforms",
    "domain-and-ssl",
    "monitoring-and-databases",
    "server-management-and-devops",
    "vps-and-dedicated-servers",
] as const;

export async function GET() {
  const baseUrl = "https://serverpicks.net";

  const urls: string[] = [];

  urls.push(`<url><loc>${baseUrl}</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>`);
  urls.push(`<url><loc>${baseUrl}/blog</loc><changefreq>weekly</changefreq><priority>0.9</priority></url>`);
  urls.push(`<url><loc>${baseUrl}/about</loc><changefreq>monthly</changefreq><priority>0.5</priority></url>`);
  urls.push(`<url><loc>${baseUrl}/contact</loc><changefreq>monthly</changefreq><priority>0.4</priority></url>`);
  urls.push(`<url><loc>${baseUrl}/faq</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>`);
  urls.push(`<url><loc>${baseUrl}/privacy</loc><changefreq>yearly</changefreq><priority>0.3</priority></url>`);
  urls.push(`<url><loc>${baseUrl}/terms</loc><changefreq>yearly</changefreq><priority>0.3</priority></url>`);
  urls.push(`<url><loc>${baseUrl}/disclosure</loc><changefreq>yearly</changefreq><priority>0.3</priority></url>`);

  for (const slug of CATEGORY_SLUGS) {
    urls.push(`<url><loc>${baseUrl}/category/${slug}</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>`);
  }

  for (const slug of BLOG_SLUGS) {
    urls.push(`<url><loc>${baseUrl}/blog/${slug}</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>`);
  }

  for (const slug of TOOL_SLUGS) {
    urls.push(`<url><loc>${baseUrl}/tools/${slug}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>`);
  }

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.join("\n")}\n</urlset>`;

  return new Response(sitemap, {
    headers: { "Content-Type": "application/xml" },
  });
}
