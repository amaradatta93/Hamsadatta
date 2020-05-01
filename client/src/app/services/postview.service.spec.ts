import { TestBed } from '@angular/core/testing';

import { PostviewService } from './postview.service';

describe('PostviewService', () => {
  let service: PostviewService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PostviewService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
