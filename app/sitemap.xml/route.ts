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
  "cross-border-ecommerce-cloud-server-guide-2026",
  "cloud-server-monitoring-2026-essentials",
  "vps-auto-scaling-strategies-2026-0622",
  "vps-vs-cloud-vs-dedicated-server-2026",
  "vps-monitoring-tools-2026-datadog-grafana-prometheus-nagios",
  "cdn-edge-computing-showdown-2026-akamai-cloudfront-fastly-cloudflare",
  "cloud-cost-optimization-strategies-startups-2026",
  "cloud-server-backup-strategies-2026",
  "hetzner-vps-saas-production-2026",
  "vps-performance-benchmarks-2026",
  "docker-on-vps-vs-kubernetes-2026",
  "vps-vs-dedicated-server-2026",
  "cloud-gpu-hosting-ai-workloads-2026",
  "vps-monitoring-observability-stack-2026",
  "vps-automation-ansible-terraform-2026",
  "vps-data-center-locations-global-coverage-2026",
  "vps-cpu-ram-storage-guide-2026",
  "dedicated-server-vs-cloud-server-2026",
  "nvme-vs-ssd-vs-object-storage-vps-2026",
  "vps-auto-scaling-strategies-2026",
  "cloud-cost-optimization-strategies-2026-0712",
  "container-registries-2026-docker-hub-ghcr-gitlab-ecr",
  "vps-migration-playbook-2026",
  "cloud-vps-network-optimization-2026",
  "vps-edge-iot-deployment-2026",
  "cdn-showdown-2026-cloudflare-stackpath-azure-cdn",
  "vps-security-solutions-2026-modsecurity-fail2ban-cloudflare-waf-ossec",
  "vps-vs-dedicated-server-comparison-2026",
  "cloud-server-vps-bare-metal-comparison-2026",
  "vps-performance-benchmarking-guide-2026",
  "cdn-performance-optimization-vps-diary-2026",
  "hetzner-vs-ovhcloud-vs-contabo-2026",
  "digitalocean-to-hetzner-migration-diary-2026",
  "vps-auto-scaling-strategies-for-2026-from-manual-to-event-driven-architecture",
  "ab-testing-vps-hetzner-digitalocean-linode-2026",
  "cloud-server-security-best-practices-2026",
  "vps-performance-comparison-hetzner-digitalocean-linode-vultr",
  "vps-wordpress-hosting-optimization-guide-2026",
  "vps-monitoring-stack-2026-grafana-prometheus-netdata",
  "cdn-vs-vps-only-architecture-2026",
  "vps-ipv6-deployment-guide-2026",
  "edge-ai-inference-vps-2026"] as const;

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
  "cloud-platforms",
  "vps-and-dedicated-servers",
  "cdn-and-dns",
  "domain-and-ssl",
  "server-management-and-devops",
  "monitoring-and-databases",
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
