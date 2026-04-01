export function getReadingTime(body: string | undefined): number {
  if (!body) return 0;
  return Math.ceil(body.split(/\s+/).length / 200);
}
